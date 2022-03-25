import sys

from werkzeug.exceptions import HTTPException

import os
import logging
from flask import Flask
from flask_jwt_extended import (
    JWTManager
)
from flask_restplus import Api
from pymongo import MongoClient
from redis import StrictRedis

from core import config
from flask_script import Manager


app = Flask(__name__)
api = Api(app)
manager = Manager(app)

app.config.from_object(
    config.config_by_name[os.getenv('FLASK_ENVIRONMENT', 'dev')]())
app.logger.info("Config: %s" % 'development')


# Create Logger object
FORMAT = '%(asctime)s %(module)s %(funcName)s %(message)s'
logging.basicConfig(filename="app.log",
                    format=FORMAT,
                    filemode='w')
logger = logging.getLogger()

jwt = JWTManager(app)
blacklist = set()
# Redis DB object
redis_store = StrictRedis(host=app.config['REDIS_HOST'],
                          port=app.config['REDIS_PORT'],
                          db=app.config['REDIS_DB'],
                          decode_responses=True)
# MongoEngine

app.db = db
app.db.init_app(app)

app.config['PROPAGATE_EXCEPTIONS'] = True


@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist

@api.errorhandler(Exception)
def handle_error(e):
    code = e.code
    message = e.__str__
    return {"status": code, "message": message}, code


@api.errorhandler(HTTPException)
def http_exception_handler(e: HTTPException):
    code = e.code
    message = e.__str__
    return {"status": code, "message": message}, code


@api.errorhandler
def default_error_handler(error):
    code = error.code
    message = error.__str__
    return {"status": code, "message": message}, code





'''from auth.auth import authapi
from users.views import users_ns
api.add_namespace(authapi, '/api/auth')
api.add_namespace(users_ns, '/api/users')


app.run(host='0.0.0.0', port=8090)'''