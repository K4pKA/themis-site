from flask import g
from flask_httpauth import HTTPBasicAuth
from app.api.errors import error_response

basic_auth = HTTPBasicAuth()


@basic_auth.error_handler
def basic_auth_error():
    return error_response(401)
