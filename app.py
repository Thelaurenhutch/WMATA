from flask import Flask, render_template, jsonify
import requests, os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv("WMATA_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/arrivals/<station_code>')
def get_arrivals(station_code):
    url = f"https://api.wmata.com/StationPrediction.svc/json/GetPrediction/{station_code}"
    headers = {'api_key': API_KEY}
    response = requests.get(url, headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
