#!/usr/bin/env python3

""" flask app
"""

from flask import Flask, jsonify, request, abort, redirect
from auth import Auth
import uuid

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'], strict_slashes=False)
def payload():
    """returns json string, aka a payload
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():  # no args
    """checked for registered users
    Args:
        None
    Returns:
        confirmation of creation of user
        or an error
    """
    try:
        # get the email and password
        email = request.form.get('email')
        password = request.form.get('password')
        # create a user object with that data
        user = AUTH.register_user(email, password)
        #  respond with the user's email and a confirmation message
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError as e:  # why does it have to be 'e'?
        return jsonify({"message": str(e)}), 400


# Define the route for user registration
@app.route("/users", methods=["POST"])
def register_user_endpoint():
    try:
        # Extract email and password from form data
        email = request.form.get("email")
        password = request.form.get("password")

        # Register the user
        register_user(email, password)

        # Respond with success message
        return jsonify({"email": email, "message": "user created"})
    except Exception as e:
        # If user is already registered
        # respond with error message and 400 status code
        return jsonify({"message": str(e)}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """i wonder what this does"""
    # get email and password from form data
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        abort(400, "Email and password are required")

    try:  # check if user is registered in the db
        if AUTH.valid_login(email, password):
            session_id = str(uuid.uuid4())
            # prepare respsonse to user login attempt
            response = jsonify({"email": email, "message": "logged in"})
            response.set_cookie('session_id', session_id)
            return response
        else:
            abort(401, "Incorrect login information")
    except ValueError:
        abort(401, "Incorrect login information")


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """i wonder what this does"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if session_id is None:
        abort(403)
    if user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    response = redirect('/')
    # response.set_cookie('session_id', '', expires=0)
    return response


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """user profilee endpoint
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if session_id is None:
        abort(403)
    if user is None:
        abort(403)
    return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """
    generate a token
    returns 200 status when successful
    """
    try:
        email = request.form.get('email')
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": token}), 200
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    """the 'update password' end point"""
    # get all the user info here
    email = request.form.get('email')
    token = request.form.get('reset_token')
    password = request.form.get('new_password')
    # check if tokens good, then update user password
    try:
        AUTH.update_password(token, password)
    except Exception as e:  # as e needed?
        abort(403)
    return jsonify({"email": email, "message": "Password updated"}), 200



if __name__ == "__main__":
    # Run the app on host 0.0.0.0 and port 5000
    app.run(host="0.0.0.0", port=5000)
