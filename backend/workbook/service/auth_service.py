# Create a service class for Authenticating users from tabke
from workbook.models.user import User


class AuthService():
    def __init__(self, db, ma):
        self.db = db
        self.ma = ma

    def authenticate(self, username, password):
        # get user from db
        user = self.db.session.query(User).filter_by(username=username).first()
        # check if user exists
        if not user:
            return False
        # check if password matches
        if user.password == password:
            return user
        return False

    def is_admin(self, user):
        if user.is_admin:
            return True
        return False
