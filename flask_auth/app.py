from flask import Flask, request, jsonify
from models.user import User
from database import db
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        login_user(user)
        return jsonify({'message': 'Logged in successfully!'})
    return jsonify({'message': 'Invalid credentials!'})

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Hello, World!'})
  
@app.route('/hello-world', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello, World!'})
  
if __name__ == '__main__':
    app.run(debug=True)