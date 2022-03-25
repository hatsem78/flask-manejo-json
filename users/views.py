from flask_jwt_extended import (
    JWTManager)
from flask_restplus import Namespace, Resource, marshal, reqparse

from users.service import UserService

jwt = JWTManager()

users_ns = Namespace('users', description='Users endpoint')

auth_parser = reqparse.RequestParser()
auth_parser.add_argument('Authorization', location='headers', required=True)

user_service = UserService()


@users_ns.route('', defaults={'user_id': None, 'completed': None, 'title': None})
@users_ns.route('/<int:user_id>', defaults={'title': None, 'completed': None})
@users_ns.route('/<int:user_id>/tasks/<completed>/<title>', defaults={'title': None})
@users_ns.route('/<int:user_id>/tasks/<completed>', defaults={'title': None})
@users_ns.route('/<int:user_id>/tasks/<title>', defaults={'title': None})
class Users(Resource):

    def get(self, user_id, completed, title):
        print(id)
        if completed is not None and completed not in "true, false":
            return {"msg-error": "variable completed no es valido, tiene que ser false o true"}

        return user_service.json_user_read(user_id, completed, title)
