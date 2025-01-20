import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

if os.environ.get("AUTH_TYPE") == 'SELF_CODED':
    from flask import Flask, jsonify, render_template
    from flask_socketio import SocketIO, emit
    from flask_cors import CORS

    from src.app.routes.auth_routes import auth_routes_bp
    from src.app.routes.user_routes import user_routes_bp
    from src.app.routes.ai_routes import ai_routes_bp

    app = Flask(__name__, template_folder="../../views/templates")
    socketio = SocketIO(app)
    CORS(app)

    # Home route
    @app.route("/", methods=["GET"])
    def home():
        return jsonify({"message": "Home!"})

    # Hello World route
    @app.route("/hello-world", methods=["GET"])
    def hello_world():
        return jsonify({"message": "Hello World!"})
    
    # Chat - SocketIO
    @app.route("/chat", methods=["GET"])
    def chat():
        return render_template("chat.html")
    
    @socketio.on('message')
    def handle_message(msg):
        emit('message', msg, broadcast=True)
        print(msg)

    app.register_blueprint(auth_routes_bp, url_prefix="/auth")
    app.register_blueprint(user_routes_bp, url_prefix="/user")
    app.register_blueprint(ai_routes_bp, url_prefix="/ai")

elif os.environ.get("AUTH_TYPE") == 'FLASK_LOGIN':
    from flask_login import LoginManager

    from flask import Flask, jsonify, render_template
    from flask_socketio import SocketIO, emit
    from src.models.repositories.user_repository import UserRepository
    from flask_cors import CORS
    from src.configs.connection import db_connection_handler

    from src.app.routes.auth_routes import auth_routes_bp
    from src.app.routes.user_routes import user_routes_bp
    from src.app.routes.ai_routes import ai_routes_bp

    app = Flask(__name__, template_folder="../../views/templates")
    socketio = SocketIO(app)
    app.secret_key = os.environ.get("FLASK_SECRET_KEY")
    CORS(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user_routes.login'

    @login_manager.user_loader
    def load_user(user_id):
        conn = db_connection_handler
        conn.connect_to_db()
        return UserRepository(conn).get_user_by_id(user_id)

    # Home route
    @app.route("/", methods=["GET"])
    def home():
        return jsonify({"message": "Home!"})

    # Hello World route
    @app.route("/hello-world", methods=["GET"])
    def hello_world():
        return jsonify({"message": "Hello World!"})

    # Chat - SocketIO
    @app.route("/chat", methods=["GET"])
    def chat():
        return render_template("chat.html")
    
    @socketio.on('message')
    def handle_message(msg):
        emit('message', msg, broadcast=True)

    app.register_blueprint(auth_routes_bp, url_prefix="/auth")
    app.register_blueprint(user_routes_bp, url_prefix="/user")
    app.register_blueprint(ai_routes_bp, url_prefix="/ai")

elif os.environ.get("AUTH_TYPE") == 'FIREBASE':
    import src.configs.firebase.firebase_config # pylint: disable=W0611
    
    from flask import Flask, jsonify, render_template
    from flask_socketio import SocketIO, emit
    from flask_cors import CORS
    
    from src.app.routes.auth_routes import auth_routes_bp
    from src.app.routes.user_routes import user_routes_bp
    # from src.app.routes.ai_routes import ai_routes_bp
    
    app = Flask(__name__, template_folder="../../views/templates")
    socketio = SocketIO(app)
    app.secret_key = os.environ.get("FLASK_SECRET_KEY")
    CORS(app)

    # Home route
    @app.route("/", methods=["GET"])
    def home():
        return jsonify({"message": "Home!"})

    # Hello World route
    @app.route("/hello-world", methods=["GET"])
    def hello_world():
        return jsonify({"message": "Hello World!"})

    # Chat - SocketIO
    @app.route("/chat", methods=["GET"])
    def chat():
        return render_template("chat.html")
    
    @socketio.on('message')
    def handle_message(msg):
        emit('message', msg, broadcast=True)

    app.register_blueprint(auth_routes_bp, url_prefix="/auth")
    app.register_blueprint(user_routes_bp, url_prefix="/user")
    # app.register_blueprint(ai_routes_bp, url_prefix="/ai")

else:
    raise Exception("Undefined authentication process.") # pylint: disable=W0719