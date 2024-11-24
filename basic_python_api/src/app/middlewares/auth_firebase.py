from firebase_admin import auth
from flask import request
from src.errors.types.http_unauthorized import HttpUnauthorizedError
from src.errors.types.http_not_found import HttpNotFoundError

def verify_firebase_token():
    """Middleware to verify Firebase ID token."""
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HttpUnauthorizedError("Invalid Auth information")

    token = auth_header.split(" ")[1]
    try:
        decoded_token = auth.verify_id_token(token)
        user_id = decoded_token["uid"]
        return user_id
    except Exception as e:
        raise HttpNotFoundError(str(e)) from e
