# ----------------------------------------------------------
# File: database.py
# Purpose: This file sets up the database connection.
# It creates the engine, session maker, and initializes the tables.
# SQLAlchemy is used to connect and interact with the MySQL database.
# ----------------------------------------------------------

from sqlalchemy import create_engine                 # Used to create the database connection
from sqlalchemy.orm import sessionmaker              # Used to create session objects
from .models import Base                             # Import the Base class from models

# ----------------------------------------------------------
# Database connection string
# Format: dialect+driver://username:password@host/database
# This connects to a MySQL database called 'talentotechcs'
# with user 'fastapi_user' and password 'kali'
# ----------------------------------------------------------
DATABASE_URL = "mysql+pymysql://fastapi_user:kali@localhost/talentotechcs"

# Create the database engine
# The engine is the core interface to the database
engine = create_engine(DATABASE_URL)

# Create a session factory
# Sessions are used to interact with the database (read/write)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables defined in the models (if they don't already exist)
Base.metadata.create_all(bind=engine)
