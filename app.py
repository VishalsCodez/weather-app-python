from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv('OPENWEATHER_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')
    weather_data = get_weather(city)
    forecast_data = get_forecast(city)
    if weather_data and forecast_data:
        return render_template('index.html', weather=weather_data, forecast=forecast_data)
    else:
        error = "Could not retrieve weather data. Please check the city name and try again."
        return render_template('index.html', error=error)

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/location_weather', methods=['POST'])
def location_weather():
    latitude = request.json['latitude']
    longitude = request.json['longitude']
    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error fetching location-based weather data: {e}")
        return jsonify({'error': 'Could not retrieve weather data'}), 500

def get_weather(city):
    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def get_forecast(city):
    try:
        url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()['list'][:5]  # Return the first 5 entries for a 5-day forecast
    except requests.exceptions.RequestException as e:
        print(f"Error fetching forecast data: {e}")
        return []

if __name__ == '__main__':
    app.run(debug=True)
