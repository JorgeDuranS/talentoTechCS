# Talentotech Login System with FastAPI

This is a web application built with **FastAPI**, **Jinja2**, and **SQLAlchemy** that simulates a user login system with basic authentication features. It includes:

- User registration
- Login with email and password
- CAPTCHA simulation ("I am not a robot" checkbox)
- Welcome page with a fun Pokédex API integration
- HTML frontend styled using TailwindCSS
- MySQL database for storing users

---

## 🧩 Project StructureS

```
.
├── app/
│   ├── main.py
│   ├── crud.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── __init__.py
├── frontend/
│   ├── index.html
│   └── welcome.html
├── requirements.txt
```

---

## 📦 Requirements

- Python 3.8 or higher
- MySQL Server running locally

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/JorgeDuranS/talentoTechCS/
cd talentoTechCS
```

### 2. Create a virtual environment

✅ On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

✅ On Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL database

Make sure you have a MySQL server running and create a database:

```sql
CREATE DATABASE talentotechcs;
```

Update the connection string in `app/database.py` if needed:

```python
DATABASE_URL = "mysql+pymysql://fastapi_user:kali@localhost/talentotechcs"
```

### 5. Run the application

From the root folder:

```bash
uvicorn app.main:app --reload
```

Then open your browser and go to:

```
http://127.0.0.1:8000/
```

---

## 🌐 Routes Overview

| Method | Path                 | Description                     |
|--------|----------------------|---------------------------------|
| GET    | /                    | Login form page                 |
| POST   | /api/login           | Login authentication            |
| POST   | /api/usuarios        | Register new user               |
| PUT    | /api/usuarios/{id}   | Update user info                |
| DELETE | /api/usuarios/{id}   | Delete (or deactivate) user     |
| GET    | /welcome             | Welcome page with Pokédex search|

---

## 📷 Frontend Features

- Login form with email, password, and a fake CAPTCHA checkbox.
- Welcome page with Pokémon search via PokéAPI.

---

## 🔒 Notes

- Passwords are securely stored using bcrypt hashing.
- CORS is enabled for development.

**Future improvements could include:**

- JWT authentication
- Soft delete using an `is_active` field
- Real CAPTCHA integration

---

## 🛠️ Author

**Talentotech Prototype by Jorge**  
Built with FastAPI, MySQL, TailwindCSS, and PokéAPI.

---


---

## 🛠️ Installing MariaDB and Setting Up the Database on Linux

### 1. Install MariaDB

On Debian/Ubuntu:

```bash
sudo apt update
sudo apt install mariadb-server
```

Start the service and enable it to run on boot:

```bash
sudo systemctl start mariadb
sudo systemctl enable mariadb
```

### 2. Secure MariaDB Installation (Optional but recommended)

```bash
sudo mysql_secure_installation
```

Follow the prompts to set a root password and secure your setup.

### 3. Log into MariaDB

```bash
sudo mariadb -u root -p
```

### 4. Create a new database and user

```sql
CREATE DATABASE talentoTechCS;
CREATE USER 'fastapi_user'@'localhost' IDENTIFIED BY 'kali';
GRANT ALL PRIVILEGES ON talentoTechCS.* TO 'fastapi_user'@'localhost';
FLUSH PRIVILEGES;
```

### 5. Create the `usuarios` table

Based on the schema in `schemas.py`, the corresponding SQL for the table would be:

```sql
USE talentoTechCS;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
```

This sets up a table that matches the structure defined in the `UsuarioLogin` schema, using `username` as an email and `password` as a plain string (note: it should be stored hashed).


## 🧪 License

This project is for educational and prototype purposes only.