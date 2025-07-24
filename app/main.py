from fastapi import FastAPI, Form, Request, status
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Usuario
from .database import SessionLocal
from .crud import get_usuario_by_email, verificar_password, crear_usuario, actualizar_usuario, desactivar_usuario


import re
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
templates = Jinja2Templates(directory="frontend")

# Habilitar CORS para todos los orígenes (desarrollo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# # Diccionario de usuarios de ejemplo
# USERS = {    
#     "jorge@kali.com": "jorge123",
#     "talentotech@kali.com": "talento123",
#     "test@kali.com": "test123",
# }

@app.get("/", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



# Endpoint para crear usuario
@app.post("/api/usuarios")
async def api_crear_usuario(username: str = Form(...), password: str = Form(...)):
    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", username):
        return JSONResponse({"error": "Correo inválido."}, status_code=status.HTTP_400_BAD_REQUEST)
    db = SessionLocal()
    if get_usuario_by_email(db, username):
        db.close()
        return JSONResponse({"error": "El usuario ya existe."}, status_code=status.HTTP_409_CONFLICT)
    user = crear_usuario(db, username, password)
    db.close()
    return JSONResponse({"success": True, "id": user.id, "email": user.email})

# Endpoint para actualizar usuario
@app.put("/api/usuarios/{user_id}")
async def api_actualizar_usuario(user_id: int, email: str = Form(None), password: str = Form(None)):
    db = SessionLocal()
    user = actualizar_usuario(db, user_id, email, password)
    db.close()
    if not user:
        return JSONResponse({"error": "Usuario no encontrado."}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse({"success": True, "id": user.id, "email": user.email})

# Endpoint para eliminar (desactivar) usuario
@app.delete("/api/usuarios/{user_id}")
async def api_desactivar_usuario(user_id: int):
    db = SessionLocal()
    result = desactivar_usuario(db, user_id)
    db.close()
    if not result:
        return JSONResponse({"error": "Usuario no encontrado."}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse({"success": True})

@app.post("/api/login")
async def api_login(username: str = Form(...), password: str = Form(...)):
    # Validar formato de correo electrónico:
    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", username):
        return JSONResponse({"error": "Por favor ingresa un correo válido."}, status_code=status.HTTP_400_BAD_REQUEST)

    db = SessionLocal()
    user = get_usuario_by_email(db, username)
    db.close()
    if user and verificar_password(password, user.password):
        return JSONResponse({"success": True})
    return JSONResponse({"error": "Credenciales inválidas. Inténtalo de nuevo."}, status_code=status.HTTP_401_UNAUTHORIZED)

@app.get("/welcome", response_class=HTMLResponse)
def welcome(request: Request):
    return templates.TemplateResponse("welcome.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
