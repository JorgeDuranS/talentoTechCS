# ----------------------------------------------------------
# File: models.py
# Purpose: This file defines the database structure (tables)
# using SQLAlchemy ORM (Object-Relational Mapping).
# Each class represents a table, and each attribute is a column.
# ----------------------------------------------------------

from sqlalchemy import Column, Integer, String  # Import tools to define table columns
from sqlalchemy.ext.declarative import declarative_base  # Base class for SQLAlchemy models

# Create a base class for all database models
Base = declarative_base()

# -----------------------------------------------
# Class: Usuario
# Represents the "usuarios" table in the database.
# Each instance of this class is one user record.
# -----------------------------------------------
class Usuario(Base):
    __tablename__ = "usuarios"  # Name of the table in the database

    # Primary key (unique ID) that auto-increments
    id = Column(Integer, primary_key=True, autoincrement=True)

    # Email column: must be unique and not empty
    email = Column(String(255), unique=True, nullable=False)

    # Password column: stores the hashed password
    password = Column(String(255), nullable=False)
