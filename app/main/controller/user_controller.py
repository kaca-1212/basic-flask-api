from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto
from ..service.user_service import save_new_user

api = UserDto.api
_user = UserDto.user


@api.route('/')
class User(Resource):
    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('Create a new user. Created user will be admin for the purpose of testing.')
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)




