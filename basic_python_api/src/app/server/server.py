import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

if os.environ.get("AUTH_TYPE") == 'SELF_CODED':
    from flask import Flask, jsonify
    from src.models.entities.user import User
    from flask_cors import CORS
    from src.configs.connection import db_connection_handler

    from src.configs.base import Base

    from src.app.routes.auth_routes import auth_routes_bp
    from src.app.routes.user_routes import user_routes_bp
    from src.app.routes.ai_routes import ai_routes_bp

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

    app.register_blueprint(auth_routes_bp, url_prefix="/auth")
    app.register_blueprint(user_routes_bp, url_prefix="/user")
    app.register_blueprint(ai_routes_bp, url_prefix="/ai")

elif os.environ.get("AUTH_TYPE") == 'FLASK_LOGIN':
    from flask_login import LoginManager, login_required

    from flask import Flask, jsonify
    from src.models.entities.user import User
    from flask_cors import CORS
    from src.configs.connection import db_connection_handler

    from src.configs.base import Base

    from src.app.routes.user_routes import user_routes_bp
    from src.app.routes.ai_routes import ai_routes_bp

    app = Flask(__name__)
    CORS(app)

    login_manager = LoginManager()
    db_connection_handler.connect_to_db(Base)
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    # Home route
    @app.route("/", methods=["GET"])
    def home():
        return jsonify({"message": "Home!"})

    # Hello World route
    @app.route("/hello-world", methods=["GET"])
    @login_required
    def hello_world():
        return jsonify({"message": "Hello World!"})

    app.register_blueprint(user_routes_bp, url_prefix="/user")

    app.register_blueprint(ai_routes_bp, url_prefix="/ai")
