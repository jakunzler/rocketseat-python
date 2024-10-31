from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest

from src.app.composer.user.create_user_composer import create_user_composer
from src.app.composer.user.login_user_composer import login_user_composer

from src.app.middlewares.auth_jwt import auth_jwt_verify

from src.errors.error_handler import handle_errors

user_routes_bp = Blueprint("user_routes", __name__)

@user_routes_bp.route("/", methods=["GET"])
def home():
    return jsonify({"message": "User: Home!"})

@user_routes_bp.route("/hello-world", methods=["GET"])
def hello_world():
    auth_jwt_verify()
    return jsonify({"message": "User: Hello World!"})

@user_routes_bp.route("/login", methods=["POST"])
def create_login():
    try:
        http_request = HttpRequest(body=request.json)
        http_response = login_user_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception: # pylint: disable=broad-except
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@user_routes_bp.route("/", methods=["POST"])
def create_user():
    try:
        http_request = HttpRequest(body=request.json)
        http_response = create_user_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception: # pylint: disable=broad-except
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@user_routes_bp.route("/users", methods=["GET"])
def get_users():
    return jsonify({"message": "User: Get Users!"})

@user_routes_bp.route("<user_id>", methods=["GET"])
def get_user(user_id):
    return jsonify({"message": "User: Get User {}!".format(user_id)})

@user_routes_bp.route("<user_id>", methods=["PUT"])
def update_user(user_id):
    return jsonify({"message": "User: Update User with ID {}".format(user_id)})

@user_routes_bp.route("<user_id>", methods=["DELETE"])
def delete_user(user_id):
    return jsonify({"message": "User: Delete User!"})

@user_routes_bp.route("<user_id>", methods=["PATCH"])
def patch_user(user_id):
    return jsonify({"message": "User: Patch User!"})
