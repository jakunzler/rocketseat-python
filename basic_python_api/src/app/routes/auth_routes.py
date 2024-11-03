import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

if os.environ.get("AUTH_TYPE") == 'SELF_CODED':

    from flask import Blueprint, jsonify, request
    from src.views.http_types.http_request import HttpRequest

    from src.app.middlewares.auth_jwt import auth_jwt_verify

    from src.app.composer.auth.login_user_composer import login_user_composer
    from src.app.composer.auth.get_revoked_tokens_composer import get_revoked_tokens_composer
    from src.app.composer.auth.logout_user_composer import logout_user_composer

    from src.errors.error_handler import handle_errors

    auth_routes_bp = Blueprint("auth_routes", __name__)

    @auth_routes_bp.route("/", methods=["POST"])
    def create_login():
        try:
            http_request = HttpRequest(body=request.json)
            http_response = login_user_composer().handle(http_request)
            return jsonify(http_response.body), http_response.status_code
        except Exception as exception: # pylint: disable=broad-except
            http_response = handle_errors(exception)
            return jsonify(http_response.body), http_response.status_code

    @auth_routes_bp.route("/", methods=["GET"])
    def get_revoked_tokens():
        try:
            http_request = HttpRequest(body=request.json)
            http_response = get_revoked_tokens_composer().handle(http_request)
            return jsonify(http_response.body), http_response.status_code
        except Exception as exception: # pylint: disable=broad-except
            http_response = handle_errors(exception)
            return jsonify(http_response.body), http_response.status_code
    
    @auth_routes_bp.route("/", methods=["DELETE"])
    def logout_user():
        try:
            auth_jwt_verify()
            http_request = HttpRequest(headers=request.headers)
            http_response = logout_user_composer().handle(http_request)
            return jsonify(http_response.body), http_response.status_code
        except Exception as exception: # pylint: disable=broad-except
            http_response = handle_errors(exception)
            return jsonify(http_response.body), http_response.status_code
        

elif os.environ.get("AUTH_TYPE") == 'FLASK_LOGIN':
    from flask import Blueprint, jsonify, request
    from src.views.http_types.http_request import HttpRequest

    from src.errors.error_handler import handle_errors

    from flask_login import login_user, current_user, logout_user, login_required

    auth_routes_bp = Blueprint("auth_routes", __name__)

    @auth_routes_bp.route("/login", methods=["POST"])
    def create_login():
        try:
            http_request = HttpRequest(body=request.json)
            http_response = login_user_composer().handle(http_request)
            return jsonify(http_response.body), http_response.status_code
        except Exception as exception: # pylint: disable=broad-except
            http_response = handle_errors(exception)
            return jsonify(http_response.body), http_response.status_code

    @auth_routes_bp.route("/logout", methods=["POST"])
    def create_logout():
        return jsonify({"message": "User: Logout!"})

else:
    raise Exception("Undefined authentication process.") # pylint: disable=W0719