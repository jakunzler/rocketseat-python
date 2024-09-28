from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Configurações básicas
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

    # Inicialização de extensões
    db.init_app(app)
    migrate.init_app(app, db)  # Inicializa o Flask-Migrate com o app Flask
    jwt.init_app(app)

    # Importa rotas
    from .routes import api
    app.register_blueprint(api)

    return app
