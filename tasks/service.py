import json
import os
from utils.db_utils import Base

base_obj = Base()


class TaskService(object):
    """
        Service Class for task View
    """

    @staticmethod
    def json_task_read(valid=None, title=None, ids=None):
        """
            get all the task
        :return:
        """

        try:

            SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
            json_url = os.path.join(SITE_ROOT.replace('tasks', ''), "static/", "tasks.json")
            data = json.load(open(json_url))

            data = sorted(data, key=lambda d: d['user_id'])

            if valid is not None:
                data = list(filter(lambda x: bool(x['completed']) == valid, data))
            elif valid is not None and title is not None:
                data = list(filter(lambda x: bool(x['completed']) == valid and x['title'] == title, data))
            elif valid is None and title is not None:
                data = list(filter(lambda x: x['title'] == title, data))
            elif ids is not None:
                data = list(filter(lambda x: x['id'] == ids, data))

            return {'total_items:': len(data), 'data': data}

        except Exception as err:
            return {'msg': err, 'code': 0}
