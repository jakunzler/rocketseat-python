import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

if os.environ.get("AUTH_TYPE") == 'SELF_CODED':

    from flask import Blueprint, jsonify, request
    from src.views.http_types.http_request import HttpRequest

    from src.app.middlewares.auth_jwt import auth_jwt_verify

    from src.app.composer.user.create_user_composer import create_user_composer

    from src.errors.error_handler import handle_errors

    user_routes_bp = Blueprint("user_routes", __name__)

    @user_routes_bp.route("/", methods=["POST"])
    def create_user():
        try:
            http_request = HttpRequest(body=request.json)
            http_response = create_user_composer().handle(http_request)
            return jsonify(http_response.body), http_response.status_code
        except Exception as exception: # pylint: disable=broad-except
            http_response = handle_errors(exception)
            return jsonify(http_response.body), http_response.status_code

    @user_routes_bp.route("/", methods=["GET"])
    def get_users():
        auth_jwt_verify()
        return jsonify({"message": "User: Get Users!"})

    @user_routes_bp.route("<user_id>", methods=["GET"])
    def get_user(user_id):
        auth_jwt_verify()
        return jsonify({"message": "User: Get User {}!".format(user_id)})

    @user_routes_bp.route("<user_id>", methods=["PUT"])
    def update_user(user_id):
        auth_jwt_verify()
        return jsonify({"message": "User: Update User with ID {}".format(user_id)})

    @user_routes_bp.route("<user_id>", methods=["DELETE"])
    def delete_user(user_id):
        auth_jwt_verify()
        return jsonify({"message": "User: Delete User!"})

    @user_routes_bp.route("<user_id>", methods=["PATCH"])
    def patch_user(user_id):
        auth_jwt_verify()
        return jsonify({"message": "User: Patch User!"})

elif os.environ.get("AUTH_TYPE") == 'FLASK_LOGIN':
    from flask import Blueprint, jsonify, request
    from src.views.http_types.http_request import HttpRequest

    from src.app.composer.user.create_user_composer import create_user_composer

    from src.errors.error_handler import handle_errors

    from flask_login import login_user, current_user, logout_user, login_required

    user_routes_bp = Blueprint("user_routes", __name__)

    @user_routes_bp.route("/", methods=["GET"])
    def home():
        return jsonify({"message": "User: Home!"})

    @user_routes_bp.route("/hello-world", methods=["GET"])
    @login_required
    def hello_world():
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

    @user_routes_bp.route("/logout", methods=["POST"])
    def create_logout():
        return jsonify({"message": "User: Logout!"})

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

else:
    raise Exception("Undefined authentication process.") # pylint: disable=W0719