from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

# OpenWeatherMap API key
API_KEY = "cefb9d99cecdefb55752d197c9a8a54b"  # Replace with your key

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', 'London')  # Default city is London
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "City not found or API request failed"}), response.status_code

    data = response.json()
    return jsonify({
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "icon": data["weather"][0]["icon"]
    })

@app.route('/forecast', methods=['GET'])
def get_forecast():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City not provided"}), 400

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "City not found or API request failed"}), response.status_code

    data = response.json()
    forecast = []
    for entry in data['list']:
        forecast.append({
            "datetime": entry['dt'],
            "temperature": entry['main']['temp'],
            "description": entry['weather'][0]['description'],
            "icon": entry['weather'][0]['icon']
        })

    return jsonify({
        "city": data['city']['name'],
        "forecast": forecast
    })

if __name__ == "__main__":
    app.run(debug=True)
