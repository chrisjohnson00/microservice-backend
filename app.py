from flask import Flask
from flask import Response

app = Flask(__name__)


@app.route('/')
def hello():
    return "Welcome the Microservice Backend!"


@app.route('/health')
def health_check():
    return "Success"


@app.route('/api/v1/foobar')
def api():
    return Response('{"foo":"bar"}', mimetype='application/json')
