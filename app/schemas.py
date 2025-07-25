# ----------------------------------------------------------
# File: schemas.py
# Purpose: This file defines data structures using Pydantic.
# These "schemas" help validate and control the data that
# comes in (e.g., from user input) and goes out (e.g., in responses).
# ----------------------------------------------------------

from pydantic import BaseModel, EmailStr  # Tools for creating and validating data models

# -----------------------------------------------
# Schema for user login
# Used to validate login form data (email & password)
# -----------------------------------------------
class UsuarioLogin(BaseModel):
    username: EmailStr  # Requires input to be a valid email address
    password: str        # Plain password as a string
