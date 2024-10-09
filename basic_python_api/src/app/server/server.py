from flask import Flask
from src.configs.connection import db_connection_handler

from src.app.routes.user_routes import user_routes_bp

db_connection_handler.connect_to_db()

app = Flask(__name__)

app.register_blueprint(user_routes_bp)
