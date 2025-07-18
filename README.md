# TalentoTechCS

This project is a basic web application built with FastAPI. It provides a login form and a welcome page.


## Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

## Installation

1. Clone this repository by running the following command in your terminal:

   ```bash
   git clone https://github.com/JorgeDuranS/talentoTechCS.git
   ```

2. Navigate to the project directory:

   ```bash
   cd talentoTechCS
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows use: venv\Scripts\activate
   ```

4. Install the required dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the server by running the following command:

   ```bash
   python main.py
   ```

2. Open a web browser and go to `http://127.0.0.1:8000` to access the application.

## Project Structure

- `main.py`: Main file containing the application logic.
- `requirements.txt`: File listing the required dependencies.
- `frontend/`: Folder containing the HTML templates.
  - `index.html`: Main page with the login form.
  - `welcome.html`: Welcome page displayed after logging in.

## Notes

- Ensure that port `8000` is available before running the application.
- If you need to change the port or host address, edit the corresponding line in `main.py`.
- To deactivate the virtual environment, use the `deactivate` command.


