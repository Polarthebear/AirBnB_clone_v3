#!/usr/bin/python3
"""Index script to connect to API"""

from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
from models import storage

hbnbText = {
	"amenities": "Amenity",
	"cities": "City",
	"places": "Place",
	"reviews": "Review",
	"states": "State",
	"users": "User"
}


@app_views.route('/status', strict_slashes=False)
def status():
     """HBNB Status"""
     return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def stats():
     """HBNB Stats"""
     return_hbnb = {}
     for key, value in hbnbText.items():
	return_hbnb[key] = storage.count(value)
     return jsonify(return_hbnb)

if __name__ == ""__main__"":
    pass
