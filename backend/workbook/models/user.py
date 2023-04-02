from workbook.app import db, ma


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100), unique=True)

    def __init__(self, username, password, email, name):
        self.username = username
        self.password = password
        self.email = email
        self.name = name

    def __repr__(self):
        # return as Name <email>
        return f'{self.name} <{self.email}>'


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'name')


# init schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)
