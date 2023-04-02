

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    # user reference to project as manager
    manager_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, description, start_date, end_date, manager_id):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.manager_id = manager_id

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.name}'


class ProjectSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description',
                  'start_date', 'end_date', 'manager_id')


product_schema = ProjectSchema()
products_schema = ProjectSchema(many=True)
