from database import db
# from sqlalchemy.dialects.postgresql import UUID
from flask_login import UserMixin

class User(db.Model, UserMixin):
    # id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=db.text("uuid_generate_v4()"))
    id = db.Column(db.Integer, primary_key=True)
    family_name = db.Column(db.String(80), unique=False, nullable=False)
    given_name = db.Column(db.String(120), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)