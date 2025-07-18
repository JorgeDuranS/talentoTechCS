from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from uvicorn import run
import os

# Create the FastAPI app
app = FastAPI()

# Set up Jinja2 templates
templates = Jinja2Templates(directory="frontend")

@app.get("/", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/welcome", response_class=HTMLResponse)
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "'or 1=1":
        return templates.TemplateResponse("welcome.html", {"request": request})
    return templates.TemplateResponse("index.html", {"request": request, "error": "Invalid credentials. Please try again."})

if __name__ == "__main__":
        run("main:app", host="127.0.0.1", port=8000, reload=True)


