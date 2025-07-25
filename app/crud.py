# ----------------------------------------------------------
# File: crud.py
# Purpose: This file contains functions for interacting with
# the database. CRUD stands for Create, Read, Update, Delete.
# These functions allow the app to manage users in the database.
# ----------------------------------------------------------

from sqlalchemy.orm import Session  # Used to work with the database session
from passlib.hash import bcrypt     # Library for hashing and verifying passwords
from .models import Usuario         # Import the user model (represents a database table)

# -------------------------------
# Read: Get user by email
# -------------------------------
def get_usuario_by_email(db: Session, email: str):
    # Query the database for the first user with the given email
    return db.query(Usuario).filter(Usuario.email == email).first()

# -------------------------------
# Utility: Verify a password
# -------------------------------
def verificar_password(password_plain: str, password_hash: str) -> bool:
    # Compare plain text password with the hashed one
    return bcrypt.verify(password_plain, password_hash)

# -------------------------------
# Create: Add a new user
# -------------------------------
def crear_usuario(db: Session, email: str, password: str):
    # Hash the user's password before saving it
    hashed = bcrypt.hash(password)

    # Create a new Usuario object (represents a database row)
    user = Usuario(email=email, password=hashed)

    # Add the new user to the session and save it to the database
    db.add(user)
    db.commit()
    db.refresh(user)  # Refresh the user object with updated data (e.g., auto-generated ID)

    return user

# -------------------------------
# Update: Modify user data
# -------------------------------
def actualizar_usuario(db: Session, user_id: int, email: str = None, password: str = None):
    # Find the user by their ID
    user = db.query(Usuario).filter(Usuario.id == user_id).first()

    # If no user is found, return None
    if not user:
        return None

    # Update fields only if new values are provided
    if email:
        user.email = email
    if password:
        user.password = bcrypt.hash(password)

    # Save the changes to the database
    db.commit()
    db.refresh(user)

    return user

# -------------------------------
# Delete (or deactivate) a user
# -------------------------------
def desactivar_usuario(db: Session, user_id: int):
    # Find the user by ID
    user = db.query(Usuario).filter(Usuario.id == user_id).first()

    # If user not found, return None
    if not user:
        return None

    # Option 1 (recommended): Use a logical delete by setting a field like `active = False`
    # Option 2 (current): Permanently delete the user from the database
    db.delete(user)
    db.commit()

    return True
