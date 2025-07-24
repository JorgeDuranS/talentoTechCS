from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from talentoTechCS.app.models import Usuario

def get_usuario_by_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()

def verificar_password(password_plain: str, password_hash: str) -> bool:
    return bcrypt.verify(password_plain, password_hash)

def crear_usuario(db: Session, email: str, password: str):
    hashed = bcrypt.hash(password)
    user = Usuario(email=email, password=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def actualizar_usuario(db: Session, user_id: int, email: str = None, password: str = None):
    user = db.query(Usuario).filter(Usuario.id == user_id).first()
    if not user:
        return None
    if email:
        user.email = email
    if password:
        user.password = bcrypt.hash(password)
    db.commit()
    db.refresh(user)
    return user

def desactivar_usuario(db: Session, user_id: int):
    user = db.query(Usuario).filter(Usuario.id == user_id).first()
    if not user:
        return None
    # Desactivación lógica: puedes agregar un campo 'activo' en el modelo y aquí ponerlo en False
    # Si no existe, aquí solo lo eliminamos
    db.delete(user)
    db.commit()
    return True
