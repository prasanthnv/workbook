from workbook.app import api
from workbook.controllers.user import UserController, UserListController
# initiate routes for workbook


def init_routes():
    api.add_resource(UserListController, '/users')
    api.add_resource(UserController, '/users/<id>')
