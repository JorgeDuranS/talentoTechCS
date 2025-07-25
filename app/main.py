# ------------------------------------------------------
# File: main.py
# Purpose: This is the main file of the web application.
# It defines the routes (URLs) and how the app responds to each one.
# It uses FastAPI to handle requests, connect to the database,
# and render HTML templates for the user interface.
# ------------------------------------------------------

# Import necessary tools from FastAPI and other libraries
from fastapi import FastAPI, Form, Request, status
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import internal modules and functions from this app
from .models import Usuario
from .database import SessionLocal
from .crud import get_usuario_by_email, verificar_password, crear_usuario, actualizar_usuario, desactivar_usuario

import re  # Regular expressions for pattern matching
import uvicorn  # Used to run the FastAPI app
from fastapi.middleware.cors import CORSMiddleware  # For handling cross-origin requests

# Create a new FastAPI application
app = FastAPI()

# Set the folder where HTML templates are located
templates = Jinja2Templates(directory="frontend")

# Enable CORS (Cross-Origin Resource Sharing)
# This allows the backend to receive requests from other origins (e.g., your frontend app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (development use)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------
# Route: GET /
# Purpose: Show the login form using index.html
# ---------------------------------------------
@app.get("/", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# --------------------------------------------------
# Route: POST /api/usuarios
# Purpose: Create a new user with email and password
# --------------------------------------------------
@app.post("/api/usuarios")
async def api_crear_usuario(username: str = Form(...), password: str = Form(...)):
    # Check if the email format is valid using regex
    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", username):
        return JSONResponse({"error": "Correo inválido."}, status_code=status.HTTP_400_BAD_REQUEST)

    # Create a database session
    db = SessionLocal()

    # Check if the user already exists
    if get_usuario_by_email(db, username):
        db.close()
        return JSONResponse({"error": "El usuario ya existe."}, status_code=status.HTTP_409_CONFLICT)

    # Create the user in the database
    user = crear_usuario(db, username, password)
    db.close()
    return JSONResponse({"success": True, "id": user.id, "email": user.email})

# --------------------------------------------------
# Route: PUT /api/usuarios/{user_id}
# Purpose: Update user's email and/or password
# --------------------------------------------------
@app.put("/api/usuarios/{user_id}")
async def api_actualizar_usuario(user_id: int, email: str = Form(None), password: str = Form(None)):
    db = SessionLocal()
    user = actualizar_usuario(db, user_id, email, password)
    db.close()

    # If user doesn't exist
    if not user:
        return JSONResponse({"error": "Usuario no encontrado."}, status_code=status.HTTP_404_NOT_FOUND)

    return JSONResponse({"success": True, "id": user.id, "email": user.email})

# --------------------------------------------------
# Route: DELETE /api/usuarios/{user_id}
# Purpose: "Delete" (deactivate) a user account
# --------------------------------------------------
@app.delete("/api/usuarios/{user_id}")
async def api_desactivar_usuario(user_id: int):
    db = SessionLocal()
    result = desactivar_usuario(db, user_id)
    db.close()

    # If user doesn't exist
    if not result:
        return JSONResponse({"error": "Usuario no encontrado."}, status_code=status.HTTP_404_NOT_FOUND)

    return JSONResponse({"success": True})

# --------------------------------------------------
# Route: POST /api/login
# Purpose: Login with email and password
# --------------------------------------------------
@app.post("/api/login")
async def api_login(username: str = Form(...), password: str = Form(...)):
    # Check if email format is valid
    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", username):
        return JSONResponse({"error": "Por favor ingresa un correo válido."}, status_code=status.HTTP_400_BAD_REQUEST)

    db = SessionLocal()
    user = get_usuario_by_email(db, username)
    db.close()

    # Check if user exists and password is correct
    if user and verificar_password(password, user.password):
        return JSONResponse({"success": True})

    return JSONResponse({"error": "Credenciales inválidas. Inténtalo de nuevo."}, status_code=status.HTTP_401_UNAUTHORIZED)

# --------------------------------------------------
# Route: GET /welcome
# Purpose: Show welcome page after login
# --------------------------------------------------
@app.get("/welcome", response_class=HTMLResponse)
def welcome(request: Request):
    return templates.TemplateResponse("welcome.html", {"request": request})

# --------------------------------------------------
# Main: Run the FastAPI app using Uvicorn
# Only runs if this file is executed directly
# --------------------------------------------------
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
