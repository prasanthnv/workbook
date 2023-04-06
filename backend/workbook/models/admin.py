from workbook.app import db, ma


class Admin(db.Model):
    '''Admin model'''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))


    def __init__(self, username, password, email, name):
        self.username = username
        self.password = password
        self.email = email
        self.name = name
    
    def __repr__(self):
        return f'{self.name} <{self.email}>'
    
    def __str__(self):
        return f'{self.name} <{self.email}>'
    
class AdminSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'name')

# init schema
admin_schema = AdminSchema()