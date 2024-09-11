from flask import Flask, request, jsonify
from models.user import User
from models.diet import Dish
from routes import main
from database import db
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

"""
user routes
"""

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        login_user(user)
        print(current_user.is_authenticated)
        return jsonify({'message': 'Logged in successfully!'})
    return jsonify({'message': 'Invalid credentials!'})

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully!'})

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    family_name = data.get('family_name')
    given_name = data.get('given_name')
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    is_admin = data.get('is_admin', False)
    
    if username and password:
        new_user = User(
            family_name=family_name,
            given_name=given_name,
            username=username,
            email=email,
            password=password,
            is_admin=is_admin
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully!'})
    else:
        return jsonify({'message': 'Username and password are required!'}), 400

@app.route('/users', methods=['GET'])
# @login_required
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/users/<int:id_user>', methods=['GET'])
@login_required
def get_user(id_user):
    user = User.query.get_or_404(id_user)
    return jsonify(user.to_dict())

@app.route('/users/<int:id_user>', methods=['PUT'])
@login_required
def update_user(id_user):
    data = request.get_json()
    user = User.query.get_or_404(id_user)
    
    user.family_name = data.get('family_name', user.family_name)
    user.given_name = data.get('given_name', user.given_name)
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.password = data.get('password', user.password)
    
    db.session.commit()
    return jsonify({'message': 'User updated successfully!'})

@app.route('/users/<int:id_user>', methods=['DELETE'])
@login_required
def delete_user(id_user):
    user = User.query.get_or_404(id_user)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully!'})

"""
dish routes
"""

@app.route('/dishes', methods=['POST'])
@login_required
def create_dish():
    data = request.get_json()
    dish_name = data.get('dish_name')
    dish_description = data.get('dish_description')
    is_allowed = data.get('is_allowed', False)
    
    if dish_name:
        new_dish = Dish(
            dish_name=dish_name,
            dish_description=dish_description,
            is_allowed=is_allowed
        )
        db.session.add(new_dish)
        db.session.commit()
        return jsonify({'message': 'Dish created successfully!'})
    else:
        return jsonify({'message': 'Name is required!'}), 400
    
@app.route('/dishes', methods=['GET'])
@login_required
def get_dishes():
    dishes = Dish.query.all()
    return jsonify([dish.to_dict() for dish in dishes])

@app.route('/dishes/<int:id_dish>', methods=['GET'])
@login_required
def get_dish(id_dish):
    dish = Dish.query.get_or_404(id_dish)
    return jsonify(dish.to_dict())

@app.route('/dishes/<int:id_dish>', methods=['PUT'])
@login_required
def update_dish(id_dish):
    data = request.get_json()
    dish = Dish.query.get_or_404(id_dish)
    
    dish.dish_name = data.get('dish_name', dish.dish_name)
    dish.dish_description = data.get('dish_description', dish.dish_description)
    dish.is_allowed = data.get('is_allowed', dish.is_allowed)
    
    db.session.commit()
    return jsonify({'message': 'Dish updated successfully!'})

@app.route('/dishes/<int:id_dish>', methods=['DELETE'])
@login_required
def delete_dish(id_dish):
    dish = Dish.query.get_or_404(id_dish)
    db.session.delete(dish)
    db.session.commit()
    return jsonify({'message': 'Dish deleted successfully!'})

"""
other routes
"""

@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Resource not found!'}), 404

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Hello, World!'})
  
@app.route('/hello-world', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello, World!'})
  
if __name__ == '__main__':
    app.run(debug=True)