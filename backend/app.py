from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    api_key = os.getenv('WEATHER_API_KEY')  # Store your API key in an environment variable
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "City not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
