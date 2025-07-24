from fastapi import FastAPI, Form, Request, status
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates


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

# Diccionario de usuarios de ejemplo
USERS = {    
    "jorge@kali.com": "jorge123",
    "talentotech@kali.com": "talento123",
    "test@kali.com": "test123",
}

@app.get("/", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



# Nuevo endpoint solo para API login (JSON)
@app.post("/api/login")
async def api_login(username: str = Form(...), password: str = Form(...)):
    # Validar formato de correo electrónico:
    # La expresión regular ^[^@\s]+@[^@\s]+\.[^@\s]+$ verifica que:
    # - Hay al menos un carácter antes del @ (que no sea espacio ni @)
    # - Hay al menos un carácter después del @ y antes del punto (que no sea espacio ni @)
    # - Hay al menos un carácter después del punto (que no sea espacio ni @)
    # Así se asegura que el usuario ingrese algo como usuario@dominio.com
    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", username):
        return JSONResponse({"error": "Por favor ingresa un correo válido."}, status_code=status.HTTP_400_BAD_REQUEST)
    # Validar contra el diccionario USERS
    if username in USERS and USERS[username] == password:
        return JSONResponse({"success": True})
    return JSONResponse({"error": "Credenciales inválidas. Inténtalo de nuevo."}, status_code=status.HTTP_401_UNAUTHORIZED)

@app.get("/welcome", response_class=HTMLResponse)
def welcome(request: Request):
    return templates.TemplateResponse("welcome.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
