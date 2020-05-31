from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Welcome the Microservice Backend!"


@app.route('/health')
def health_check():
    return "Success"


@app.route('/api/v1/fo0bar')
def api():
    return '{"foo":"bar"}'
