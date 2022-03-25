import os
from flask_cors.core import LOG
from tasks.views import tasks_ns
from core.resources import api, app
from users.views import users_ns

api.add_namespace(tasks_ns, '/api/tasks')
api.add_namespace(users_ns, '/api/user')


if __name__ == '__main__':

    LOG.info('running environment: %s', os.environ.get('ENV'))
    app.config['DEBUG'] = 'development' # Debug mode if development env
    app.run(host='0.0.0.0', port=8090)  # Run the app
