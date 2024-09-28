from .models import User, UserSession, db

def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:  # Ensure you hash the password in production
        return user
    return None

def create_user_session(user_id, latitude, longitude):
    session = UserSession(user_id=user_id, latitude=latitude, longitude=longitude)
    db.session.add(session)
    db.session.commit()
    return session