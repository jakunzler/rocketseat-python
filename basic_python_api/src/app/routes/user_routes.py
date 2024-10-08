from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest

from src.app.composer.user_register_composer import user_register_composer
from src.app.composer.login_creator_composer import login_creator_composer

from src.app.middlewares.auth_jwt import auth_jwt_verify

from src.errors.error_handler import handle_errors

user_routes_bp = Blueprint("user_routes", __name__)

@user_routes_bp.route("/hello-world", methods=["GET"])
def hello_world():
    return jsonify({"message": "Hello World!"})

@user_routes_bp.route("/user", methods=["POST"])
def registry_user():
    try:
        http_request = HttpRequest(body=request.json)
        http_response = user_register_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@user_routes_bp.route("/user/login", methods=["POST"])
def create_login():
    try:
        http_request = HttpRequest(body=request.json)
        http_response = login_creator_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
