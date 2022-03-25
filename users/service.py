import json
import os
from utils.db_utils import Base

base_obj = Base()


class UserService(object):
    """
        Service Class for task View
    """

    @staticmethod
    def json_user_read(user_id=None, valid=None, title=None, ids=None):
        """
            get all the task
        :return:
        """

        try:

            SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
            json_url = os.path.join(SITE_ROOT.replace('users', ''), "static/", "users.json")
            data = json.load(open(json_url))

            SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
            json_task_url = os.path.join(SITE_ROOT.replace('tasks', ''), "static/", "tasks.json")
            data_task = json.load(open(json_task_url))

            data = sorted(data, key=lambda d: d['id'])

            if user_id is not None:
                data = list(filter(lambda x: x['id'] == user_id, data))
            elif valid is not None:
                data = list(filter(lambda x: bool(x['completed']) == valid and x['user_id'] == user_id, data_task))
            elif valid is not None and title is not None:
                data = list(filter(lambda x: bool(x['completed']) == valid and x['title'] == title and x['user_id'] == user_id, data))
            elif valid is None and title is not None:
                data = list(filter(lambda x: x['title'] == title and x['user_id'] == user_id, data))

            return {'total_items:': len(data), 'data': data}

        except Exception as err:
            return {'msg': err, 'code': 0}
