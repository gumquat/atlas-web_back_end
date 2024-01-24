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
def users(email, password):
    """checked for registered users
    Args:
        email (_type_): email
        password (_type_): password
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


if __name__ == "__main__":
    # Run the app on host 0.0.0.0 and port 5000
    app.run(host="0.0.0.0", port=5000)
