from flask import Flask, jsonify
from datetime import datetime
import socket

app = Flask(__name__)


@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'


@app.route('/api/v1/details')
# ‘/’ URL is bound with details() function.
def details():
    now = datetime.now()
    return jsonify({ "time": now.strftime("%H:%M:%S"), "hostname": socket.gethostname() })         


@app.route('/api/v1/healthz')
# ‘/’ URL is bound with healthz() function.
def healthz():
    return jsonify({ "status": "up", "code": 200 })

@app.route('/api/users')
def get_users():
    users = [{'id': 1, 'username': 'Alice'}, {'id': 2, 'username': 'Bob'}]
    response = jsonify(users)
    response.status_code = 200
    response.mimetype = 'application/json'
    return response


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host='0.0.0.0', port=5000)
