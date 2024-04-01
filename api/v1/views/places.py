#!/usr/bin/python3
"""This module implement a rule that return a view"""
from flask import jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.city import City
from models.place import Place
from models.user import User
from models.state import State
from models.amenity import Amenity
from flasgger.utils import swag_from


@app_views.route("/cities/<city_id>/places", methods=["GET"],
                 strict_slashes=False)
@swag_from('documentation/place/get_places.yml', methods=['GET'])
def place_by_city(city_id):
    """View function that return place objects by city"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify([place.to_dict() for place in city.places])


@app_views.route("/places/<place_id>", methods=["GET"],
                 strict_slashes=False)
@swag_from('documentation/place/get_place.yml', methods=['GET'])
def show_place(place_id):
    """Endpoint that return a Place object"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route("/places/<place_id>", methods=["DELETE"],
                 strict_slashes=False)
@swag_from('documentation/place/delete_place.yml', methods=['DELETE'])
def delete_place(place_id):
    """Endpoint that delete a Place object"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    place.delete()
    storage.save()
    return jsonify({})
