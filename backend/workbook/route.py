from workbook.controllers.user import UserController, UserListController
from workbook.app import api
# initiate routes for workbook


def init_routes():
    api.add_resource(UserListController, '/users')
    api.add_resource(UserController, '/users/<id>')
