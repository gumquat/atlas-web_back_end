#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None

auth_type = getenv("AUTH_TYPE")
if getenv('AUTH_TYPE') == 'basic_auth':  # If the AUTH_TYPE is Basic...
    from api.v1.auth.basic_auth import BasicAuth  # ...import the class...
    auth = BasicAuth()  # ...then instantiate the class
else:  # If the AUTH_TYPE is not Basic import and insantiate a different class
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.before_request
def before_request() -> None:
    """Check if the AUTH_TYPE is Basic, if not, skip this check"""
    if auth is None:
        return

    excluded_paths = [  # List of paths to be excluded from authentication
        '/api/v1/status/',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden/']
    # Check if the path is not in the excluded paths list.
    # If the path is not in the excluded paths list,
    # check if authentication is required for the given path.
    if request.path not in excluded_paths:
        if auth and auth.require_auth(request.path, excluded_paths):
            if auth.authorization_header(request) is None:  # If no header
                abort(401)
            if auth.current_user(request) is None:  # If no user
                abort(403)
            # assign the current user to the request
            request.current_user = auth.current_user(request)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """unauthorized handler
    returns: get outta here!
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden_error(error) -> str:
    """EXOOODIAAAAA!!!"""
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
