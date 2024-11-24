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
    from src.app.composer.auth.clear_revoked_tokens_composer import clear_revoked_tokens_composer
    from src.app.composer.auth.logout_user_composer import logout_user_composer

    from src.errors.error_handler import handle_errors

    auth_routes_bp = Blueprint("auth_routes", __name__)

    @auth_routes_bp.route("/", methods=["POST"])
    def login():
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
            auth_jwt_verify()
            http_request = HttpRequest()
            http_response = get_revoked_tokens_composer().handle(http_request)
            return jsonify(http_response.body), http_response.status_code
        except Exception as exception: # pylint: disable=broad-except
            http_response = handle_errors(exception)
            return jsonify(http_response.body), http_response.status_code

    @auth_routes_bp.route("/", methods=["PUT"])
    def clear_revoked_tokens():
        try:
            auth_jwt_verify()
            http_request = HttpRequest()
            http_response = clear_revoked_tokens_composer().handle(http_request)
            return jsonify(http_response.body), http_response.status_code
        except Exception as exception: # pylint: disable=broad-except
            http_response = handle_errors(exception)
            return jsonify(http_response.body), http_response.status_code

    @auth_routes_bp.route("/", methods=["DELETE"])
    def logout():
        try:
            auth_jwt_verify()
            http_request = HttpRequest(headers=request.headers)
            http_response = logout_user_composer().handle(http_request)
            return jsonify(http_response.body), http_response.status_code
        except Exception as exception: # pylint: disable=broad-except
            http_response = handle_errors(exception)
            return jsonify(http_response.body), http_response.status_code

    # Exemplo de rota protegida dentro do blueprint
    @auth_routes_bp.route("/profile", methods=["GET"])
    def profile():
        auth_jwt_verify()
        return jsonify({"User allowed": True})

elif os.environ.get("AUTH_TYPE") == 'FLASK_LOGIN':
    from flask import Blueprint, request, jsonify
    from flask_login import login_user, login_required, logout_user, current_user

    from src.configs.connection import db_connection_handler
    from src.models.repositories.user_repository import UserRepository

    auth_routes_bp = Blueprint("auth_routes", __name__)

    @auth_routes_bp.route("/", methods=["POST"])
    def login():
        data = request.json
        conn = db_connection_handler
        conn.connect_to_db()
        user = UserRepository(conn).get_user_by_username(data["username"])

        if user:
            login_user(user)
            return jsonify({"message": "Login successful!"})
        return jsonify({"message": "Invalid credentials!"}), 401

    @auth_routes_bp.route("/", methods=["GET"])
    @login_required
    def get_revoked_tokens():
        return jsonify({"message": "Nothing to see here!"})

    @auth_routes_bp.route("/", methods=["PUT"])
    @login_required
    def clear_revoked_tokens():
        return jsonify({"message": "Nothing to see here!"})

    @auth_routes_bp.route("/", methods=["DELETE"])
    @login_required
    def logout():
        logout_user()
        return jsonify({"message": "Logged out!"})

    # Exemplo de rota protegida dentro do blueprint
    @auth_routes_bp.route("/profile", methods=["GET"])
    @login_required
    def profile():
        return jsonify({"username": current_user.username, "email": current_user.email})

elif os.environ.get("AUTH_TYPE") == 'FIREBASE':
    import requests
    from flask import Blueprint, request, jsonify
    from firebase_admin import auth
    from src.app.middlewares.auth_firebase import verify_firebase_token
    from src.errors.types.http_bad_request import HttpBadRequestError
    from src.errors.types.http_unauthorized import HttpUnauthorizedError

    auth_routes_bp = Blueprint("firebase", __name__)

    @auth_routes_bp.route("/", methods=["POST"])
    def firebase_login():
        """Authenticate with Firebase."""
        data = request.json
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            raise HttpBadRequestError("Email and password required")

        # try:
        #     # Firebase Admin doesn't allow password authentication; use client-side SDK.
        #     user = auth.get_user_by_email(email)
        #     return jsonify({"message": "User exists", "uid": user.uid}), 200
        # except Exception as e:
        #     raise HttpUnauthorizedError(str(e)) from e
        url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyDEMOUZYa1hql2i8TB_7lL2FMn3fLiJcwU"
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }
        response = requests.post(url, json=payload, timeout=(5, 15))
        if response.status_code == 200:
            return response.json()  # Retorna os tokens (idToken, refreshToken, etc.)

        raise Exception(f"Authentication failed: {response.json()}") # pylint: disable=W0719
    
    @auth_routes_bp.route("/", methods=["GET"])
    def get_revoked_tokens():
        user_id = verify_firebase_token()
        return jsonify({"message": "Access granted", "user_id": user_id}), 200
    
    @auth_routes_bp.route("/", methods=["PUT"])
    def clear_revoked_tokens():
        user_id = verify_firebase_token()
        return jsonify({"message": "Access granted", "user_id": user_id}), 200
    
    @auth_routes_bp.route("/", methods=["DELETE"])
    def logout_user():
        try:
            user_id = verify_firebase_token()
            # if user_id != uid:
            #     raise HttpUnauthorizedError("Invalid user ID")
            # Revogar todos os tokens de acesso emitidos para o usuário
            auth.revoke_refresh_tokens(user_id)
            return jsonify({"message": f"Tokens revoked for user: {user_id}"}), 200
        except Exception as e:
            raise HttpUnauthorizedError(str(e)) from e

    @auth_routes_bp.route("/profile", methods=["GET"])
    def profile():
        user_id = verify_firebase_token()
        if isinstance(user_id, dict):  # If it returned a response (error)
            return user_id
        return jsonify({"message": "Access granted", "user_id": user_id}), 200

else:
    raise Exception("Undefined authentication process.") # pylint: disable=W0719
