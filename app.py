from flask import Flask
from flask import render_template, jsonify, request
from app_db import DB

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return 'Hello World!!!!!!!!!!!!!!!'


@app.route('/id/<int:id>', methods=['GET', 'PUT'])
def id(id):
	if request.method == 'PUT':
		print request.data
	return jsonify(DB[id])


if __name__ == '__main__':
    app.run(host='0.0.0.0')
