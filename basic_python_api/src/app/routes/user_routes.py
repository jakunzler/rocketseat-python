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

elif os.environ.get("AUTH_TYPE") == 'FIREBASE':
    
    from flask import Blueprint, jsonify, request
    from firebase_admin import auth
    
    user_routes_bp = Blueprint("user_routes", __name__)

    @user_routes_bp.route("/", methods=["POST"])
    def firebase_register():
        """Register a new user with Firebase."""
        data = request.json
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"error": "Email and password required"}), 400

        try:
            new_user = auth.create_user(email=email, password=password)
            return jsonify({"message": "User created", "uid": new_user.uid}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400
        
    @user_routes_bp.route("/", methods=["GET"])
    def firebase_get_users():
        """Get all users from Firebase."""
        users_page = auth.list_users()

        # Lista para armazenar os dados dos usuários
        users = []

        # Itera sobre todos os usuários e extrai os dados relevantes
        for current_user in users_page.iterate_all():
            users.append({
                "uid": current_user.uid,
                "email": current_user.email,
                "display_name": current_user.display_name,
                "phone_number": current_user.phone_number,
                "email_verified": current_user.email_verified,
                "disabled": current_user.disabled,
                "custom_claims": current_user.custom_claims,
                "created_at": current_user.user_metadata.creation_timestamp,
                "last_sign_in_at": current_user.user_metadata.last_sign_in_timestamp
            })

        return jsonify({
            "Message": "Done",
            "users": users
        })
    
    @user_routes_bp.route("<user_id>", methods=["GET"])
    def firebase_get_user(user_id):
        """Get a user from Firebase."""
        selected_user = auth.get_user(user_id)
        
        return jsonify({
            "Message": "Done",
            "user": {
                "uid": selected_user.uid,
                "email": selected_user.email,
                "display_name": selected_user.display_name,
                "phone_number": selected_user.phone_number,
                "email_verified": selected_user.email_verified,
                "disabled": selected_user.disabled,
                "custom_claims": selected_user.custom_claims,
                "created_at": selected_user.user_metadata.creation_timestamp,
                "last_sign_in_at": selected_user.user_metadata.last_sign_in_timestamp
            }
        })
        
    @user_routes_bp.route("<user_id>", methods=["PUT"])
    def firebase_update_user(user_id):
        """Update a user from Firebase."""
        data = request.json
        try:
            auth.update_user(user_id, **data)
            return jsonify({"message": "User updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    
    @user_routes_bp.route("<user_id>", methods=["DELETE"])
    def firebase_delete_user(user_id):
        """Delete a user from Firebase."""
        auth.delete_user(user_id)
        return jsonify({"message": "User deleted"})
    
    @user_routes_bp.route("<user_id>", methods=["PATCH"])
    def firebase_update_user_attribute(user_id):
        """Update a user from Firebase."""
        data = request.json
        try:
            auth.update_user(user_id, **data)
            return jsonify({"message": "User updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 400

else:
    raise Exception("Undefined authentication process.") # pylint: disable=W0719