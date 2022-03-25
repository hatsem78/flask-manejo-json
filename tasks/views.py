from pprint import pprint

from flask_jwt_extended import (
    JWTManager)
from flask_restplus import Namespace, Resource, marshal, reqparse
from tasks.service import TaskService

jwt = JWTManager()

tasks_ns = Namespace('tasks', description='Tasks endpoint')

auth_parser = reqparse.RequestParser()
auth_parser.add_argument('Authorization', location='headers', required=True)

task_service = TaskService()


@tasks_ns.route('', defaults={'title': None, 'completed': None})
@tasks_ns.route('/<completed>', defaults={'title': None})
@tasks_ns.route('/<title>', defaults={'completed': None})
@tasks_ns.route('/<int:id>', defaults={'title': None, 'completed': None})
class Tasks(Resource):

    def get(self, completed, title, id):

        print(id)
        if completed is not None and completed not in "true, false":
            return {"msg-error": "variable completed no es valido, tiene que ser false o true"}

        return task_service.json_task_read(completed, title, id)
