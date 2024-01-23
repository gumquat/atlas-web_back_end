#!/usr/bin/env python3
"""
'Flask' handler for 'session Auth' routes
"""
from flask import request, jsonify, abort, make_response
from api.v1.views import app_views
from api.v1.app import auth
import os
from models.user import User
from os import getenv


@app_views.route('/auth_session/login',
                 methods=['POST'], strict_slashes=False)
def login():
    """session authentication route
    Returns:
        _type_: error messsage or user response
    """
    # email
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400
    # password
    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400
    # search for user via email & make user object
    users = User.search({"email": email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404
    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    # make dict object of user
    user_dict = user.to_json()

    session_id = auth.create_session(user.id)
    session_cookie_name = os.getenv('SESSION_NAME')
    response = jsonify(user_dict)
    response = make_response(response)

    response.set_cookie(session_cookie_name, session_id)

    return response


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def logout():
    """i wonder what this does
    """
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
