from flask_restful import Resource


class Auth(Resource):
    def post(self):
        return {'message': 'Hello, World!'}

    def get(self):
        return {'message': 'Hello, World!'}
    