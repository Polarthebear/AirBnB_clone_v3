#!/usr/bin/python3
"""Program that connects to API"""

import os
from models import storage
from api.v1.views import app_views
from flask_cors import CORS
from flask import Flask, Blueprint, make_response, jsonify

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.teardown_appcontext
def teardown_app(code):
	"""teardown app"""
	strorage.close()


@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
   app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
	   port=int(os.getenv('HBNB_API_PORT', '5000')))

