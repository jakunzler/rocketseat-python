from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from .controllers import authenticate_user, create_user_session
from .models import db

api = Blueprint('api', __name__)

@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    user = authenticate_user(username, password)
    if not user:
        return jsonify({"msg": "Invalid username or password"}), 401

    session = create_user_session(user.id, latitude, longitude)
    token = create_access_token(identity=user.id)
    return jsonify(token=token, session={"latitude": session.latitude, "longitude": session.longitude}), 200
