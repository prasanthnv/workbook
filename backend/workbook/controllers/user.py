from flask import jsonify, request
from flask_restful import Resource

from workbook.models.user import User, user_schema, users_schema
from workbook.app import db


class UserListController(Resource):
    # get all users
    def get(self):
        print('get all users')
        all_users = User.query.all()
        results = users_schema.dump(all_users)
        return jsonify(results)

    # create user
    def post(self):
        username = request.json['username']
        password = request.json['password']
        email = request.json['email']
        name = request.json['name']

        new_user = User(username, password, email, name)

        db.session.add(new_user)
        db.session.commit()

        return user_schema.jsonify(new_user)


class UserController(Resource):
    # get all users
    def get(self):
        print('get all users')
        all_users = User.query.all()
        results = users_schema.dump(all_users)
        return jsonify({
            'users': results
        })

    # get user by id
    def get(self, id):
        print('get user by id')
        user = User.query.get(id)
        return user_schema.jsonify(user)
