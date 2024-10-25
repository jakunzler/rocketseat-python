from flask import Flask, jsonify
from flask_cors import CORS
from src.configs.base import Base
from src.configs.connection import db_connection_handler

from src.app.routes.user_routes import user_routes_bp
from src.app.routes.ai_routes import ai_routes_bp

db_connection_handler.connect_to_db(Base)

app = Flask(__name__)
CORS(app)

# Home route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Home!"})

# Hello World route
@app.route("/hello-world", methods=["GET"])
def hello_world():
    return jsonify({"message": "Hello World!"})

app.register_blueprint(user_routes_bp, url_prefix="/user")
app.register_blueprint(ai_routes_bp, url_prefix="/ai")
