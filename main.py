from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from uvicorn import run

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>Hello World</title>
        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    </head>
    <body class='bg-gray-100 flex items-center justify-center h-screen'>
        <div class='bg-white p-8 rounded shadow text-center'>
            <h1 class='text-4xl font-bold text-gray-800 mb-4'>Hello, World!</h1>
            <p class='text-gray-600'>Bienvenido a tu app FastAPI.</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    run("main:app", host="127.0.0.1", port=8000, reload=True)


git config --global user.name "JorgeDuran"
git config --global user.email "jdurans89@gmailcom"