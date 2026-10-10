# Food Calorie Calculator

A beginner-friendly full-stack project built with HTML, CSS, JavaScript, Python, and Flask.

## Features
- Browse a sample list of common foods and estimated calories
- Add multiple foods and quantities
- Calculate the estimated total calories using a backend API
- Responsive layout for laptop and mobile
- Input validation

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. Create a virtual environment (optional but recommended):
   - Windows: `py -m venv .venv`
   - Windows PowerShell: `.venv\Scripts\Activate.ps1`
4. Install packages: `pip install -r requirements.txt`
5. Start the app: `python app.py`
6. Open `http://127.0.0.1:5000`

## API endpoints
- `GET /api/foods` — returns the food list
- `POST /api/calculate` — accepts JSON like:
  `{"items":[{"foodId":"idli","quantity":2},{"foodId":"banana","quantity":1}]}`
- `GET /` — serves the frontend

## Deploy to Render
1. Push all project files to a GitHub repository.
2. In Render, choose **New + → Web Service** and connect the repository.
3. Render can use `render.yaml`, or enter:
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
4. Deploy and open the generated `https://...onrender.com` URL.

## Notes
Calorie values are estimates and vary by serving size, ingredients, and preparation. This project is educational and is not a substitute for professional nutrition advice.
