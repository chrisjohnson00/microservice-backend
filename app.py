from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    return "Welcome the Microservice Backend!"


@app.route('/health')
def health_check():
    return "Success"


@app.route('/api/v1/fobar')
def api():
    resp = requests.get("https://status.github.com/api/status.json")
    txt = resp.text
    return txt
