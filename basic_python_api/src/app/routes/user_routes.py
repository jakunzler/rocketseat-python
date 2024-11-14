import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

if os.environ.get("AUTH_TYPE") == 'SELF_CODED':

    from flask import Blueprint, jsonify, request
    from src.views.http_types.http_request import HttpRequest

    from src.app.middlewares.auth_jwt import auth_jwt_verify

    from src.app.composer import user
    
    from src.errors.error_handler import handle_errors

    user_routes_bp = Blueprint("user_routes", __name__)

    @user_routes_bp.route("/", methods=["POST"])
    def create_user():
        try:
            http_request = HttpRequest(body=request.json)
            http_response = user.create_user_composer().handle(http_request)
            return jsonify(http_response.body), http_response.status_code
        except Exception as exception: # pylint: disable=broad-except
            http_response = handle_errors(exception)
            return jsonify(http_response.body), http_response.status_code

    @user_routes_bp.route("/", methods=["GET"])
    def get_users():
        auth_jwt_verify()
        try:
            data = request.get_json(silent=True)
            http_request = HttpRequest(body=data)
            http_response = user.get_users_composer().handle(http_request)
            return jsonify(http_response.body), http_response.status_code
        except Exception as exception: # pylint: disable=broad-except
            http_response = handle_errors(exception)
            return jsonify(http_response.body), http_response.status_code

    @user_routes_bp.route("<user_id>", methods=["GET"])
    def get_user(user_id):
        auth_jwt_verify()
        try:
            http_request = HttpRequest(params=user_id)
            http_response = user.get_user_by_id_composer().handle(http_request)
            return jsonify(http_response.body), http_response.status_code
        except Exception as exception: # pylint: disable=broad-except
            http_response = handle_errors(exception)
            return jsonify(http_response.body), http_response.status_code

    @user_routes_bp.route("<user_id>", methods=["PUT"])
    def update_user(user_id):
        auth_jwt_verify()
        try:
            http_request = HttpRequest(params=user_id, body=request.json)
            http_response = user.update_user_composer().handle(http_request)
            return jsonify(http_response.body), http_response.status_code
        except Exception as exception: # pylint: disable=broad-except
            http_response = handle_errors(exception)
            return jsonify(http_response.body), http_response.status_code

    @user_routes_bp.route("<user_id>", methods=["PATCH"])
    def patch_user(user_id):
        auth_jwt_verify()
        try:
            http_request = HttpRequest(params=user_id, body=request.json)
            http_response = user.update_user_attribute_composer().handle(http_request)
            return jsonify(http_response.body), http_response.status_code
        except Exception as exception: # pylint: disable=broad-except
            http_response = handle_errors(exception)
            return jsonify(http_response.body), http_response.status_code

    @user_routes_bp.route("<user_id>", methods=["DELETE"])
    def delete_user(user_id):
        auth_jwt_verify()
        try:
            http_request = HttpRequest(params=user_id)
            http_response = user.delete_user_by_id_composer().handle(http_request)
            return jsonify(http_response.body), http_response.status_code
        except Exception as exception: # pylint: disable=broad-except
            http_response = handle_errors(exception)
            return jsonify(http_response.body), http_response.status_code

elif os.environ.get("AUTH_TYPE") == 'FLASK_LOGIN':
    from flask import Blueprint, jsonify, request
    from src.views.http_types.http_request import HttpRequest

    from flask_login import login_required

    from src.app.composer import user

    from src.errors.error_handler import handle_errors

    user_routes_bp = Blueprint("user_routes", __name__)

    @user_routes_bp.route("/", methods=["POST"])
    @login_required
    def create_user():
        try:
            http_request = HttpRequest(body=request.json)
            http_response = user.create_user_composer().handle(http_request)
            return jsonify(http_response.body), http_response.status_code
        except Exception as exception: # pylint: disable=broad-except
            http_response = handle_errors(exception)
            return jsonify(http_response.body), http_response.status_code

    @user_routes_bp.route("/", methods=["GET"])
    @login_required
    def get_users():
        try:
            data = request.get_json(silent=True)
            http_request = HttpRequest(body=data)
            http_response = user.get_users_composer().handle(http_request)
            return jsonify(http_response.body), http_response.status_code
        except Exception as exception: # pylint: disable=broad-except
            http_response = handle_errors(exception)
            return jsonify(http_response.body), http_response.status_code

    @user_routes_bp.route("<user_id>", methods=["GET"])
    @login_required
    def get_user(user_id):
        try:
            http_request = HttpRequest(params=user_id)
            http_response = user.get_user_by_id_composer().handle(http_request)
            return jsonify(http_response.body), http_response.status_code
        except Exception as exception: # pylint: disable=broad-except
            http_response = handle_errors(exception)
            return jsonify(http_response.body), http_response.status_code

    @user_routes_bp.route("<user_id>", methods=["PUT"])
    @login_required
    def update_user(user_id):
        try:
            http_request = HttpRequest(params=user_id, body=request.json)
            http_response = user.update_user_composer().handle(http_request)
            return jsonify(http_response.body), http_response.status_code
        except Exception as exception: # pylint: disable=broad-except
            http_response = handle_errors(exception)
            return jsonify(http_response.body), http_response.status_code

    @user_routes_bp.route("<user_id>", methods=["PATCH"])
    @login_required
    def patch_user(user_id):
        try:
            http_request = HttpRequest(params=user_id, body=request.json)
            http_response = user.update_user_attribute_composer().handle(http_request)
            return jsonify(http_response.body), http_response.status_code
        except Exception as exception: # pylint: disable=broad-except
            http_response = handle_errors(exception)
            return jsonify(http_response.body), http_response.status_code

    @user_routes_bp.route("<user_id>", methods=["DELETE"])
    @login_required
    def delete_user(user_id):
        try:
            http_request = HttpRequest(params=user_id)
            http_response = user.delete_user_by_id_composer().handle(http_request)
            return jsonify(http_response.body), http_response.status_code
        except Exception as exception: # pylint: disable=broad-except
            http_response = handle_errors(exception)
            return jsonify(http_response.body), http_response.status_code

else:
    raise Exception("Undefined authentication process.") # pylint: disable=W0719