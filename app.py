from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder="static")

# Approximate calories per standard serving. Values are estimates, not medical advice.
FOODS = [
    {"id": "rice", "name": "Cooked white rice", "serving": "100 g", "calories": 130},
    {"id": "chapati", "name": "Chapati", "serving": "1 medium", "calories": 120},
    {"id": "idli", "name": "Idli", "serving": "1 piece", "calories": 58},
    {"id": "dosa", "name": "Plain dosa", "serving": "1 medium", "calories": 168},
    {"id": "upma", "name": "Upma", "serving": "100 g", "calories": 150},
    {"id": "dal", "name": "Cooked dal", "serving": "100 g", "calories": 116},
    {"id": "egg", "name": "Boiled egg", "serving": "1 large", "calories": 78},
    {"id": "banana", "name": "Banana", "serving": "1 medium", "calories": 105},
    {"id": "apple", "name": "Apple", "serving": "1 medium", "calories": 95},
    {"id": "milk", "name": "Milk", "serving": "100 ml", "calories": 61},
    {"id": "curd", "name": "Plain curd", "serving": "100 g", "calories": 98},
    {"id": "paneer", "name": "Paneer", "serving": "100 g", "calories": 265},
    {"id": "chicken", "name": "Cooked chicken breast", "serving": "100 g", "calories": 165},
    {"id": "oats", "name": "Oats (dry)", "serving": "40 g", "calories": 152},
    {"id": "almonds", "name": "Almonds", "serving": "10 pieces", "calories": 70},
]

@app.get("/")
def home():
    return send_from_directory("static", "index.html")

@app.get("/api/foods")
def get_foods():
    return jsonify({"foods": FOODS})

@app.post("/api/calculate")
def calculate():
    data = request.get_json(silent=True) or {}
    items = data.get("items", [])
    if not isinstance(items, list) or not items:
        return jsonify({"error": "Please add at least one food item."}), 400

    results = []
    total = 0
    for item in items:
        food_id = str(item.get("foodId", ""))
        try:
            quantity = float(item.get("quantity", 0))
        except (TypeError, ValueError):
            return jsonify({"error": "Quantity must be a number."}), 400
        food = next((f for f in FOODS if f["id"] == food_id), None)
        if food is None:
            return jsonify({"error": "One of the selected foods is not available."}), 400
        if quantity <= 0 or quantity > 1000:
            return jsonify({"error": "Quantity must be greater than 0 and no more than 1000 servings."}), 400
        calories = round(food["calories"] * quantity)
        total += calories
        results.append({
            "food": food["name"],
            "quantity": quantity,
            "serving": food["serving"],
            "calories": calories
        })
    return jsonify({"items": results, "totalCalories": total})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
