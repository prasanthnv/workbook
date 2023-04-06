from flask_restful import Resource
from flask import jsonify, request
from workbook.app import db, ma
from workbook.service.auth_service import AuthService


class Auth(Resource):
    def __init__(self):
        self.authService = AuthService(db, ma)

    def post(self):
        # get data from request
        data = request.get_json()
        # authenticate user
        user = self.authService.authenticate(
            data['username'], data['password'])
        # check if user exists
        if not user:
            return jsonify({'message': 'Invalid credentials'}), 401
        # check if user is admin
        if self.authService.is_admin(user):
            return jsonify({'message': 'Admin login successful'}), 200
        return jsonify({'message': 'User login successful'}), 200
