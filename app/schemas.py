from pydantic import BaseModel, EmailStr

class UsuarioLogin(BaseModel):
    username: EmailStr
    password: str
