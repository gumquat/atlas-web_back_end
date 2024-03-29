#!/usr/bin/env python3
"""
basic authentication module :nerd:
"""


from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """
    Class BasicAuth
    Inherits from Auth.py
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extract the Base64 part from the Authorization header
        Args:
            authorization_header (str): The Authorization header
        Returns:
            str: The Base64 part or None if the header is not valid
        """
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        # extracts the Base64 part after "Basic "
        # strip() removes leading and trailing spaces
        base64_part = authorization_header[len("Basic "):].strip()
        return base64_part

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decode the Base64 part of the Authorization header.
        Args:
            base64_authorization_header (str):
            The Base64 part of the Authorization header
        Returns:
            str: The decoded Base64 part or None if the decoding failed
        """
        if base64_authorization_header is None \
                or not isinstance(base64_authorization_header, str):
            return None

        try:
            # decode the Base64 string
            decoded_bytes = base64.b64decode(base64_authorization_header)
            # then convert it into a UTF-8 string
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except base64.binascii.Error:  # if decoding fails:
            # raise error if base64_authorization_header
            # is not a valid Base64 string
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """etract user credentials from decoded values
        Args:
            self (_type_):
            str (_type_):
        """
        # if the decoded_base64_authorization_header is not a valid string
        if decoded_base64_authorization_header is None or \
                not isinstance(decoded_base64_authorization_header, str):
            return None, None
        # if ':' not in string
        if ':' not in decoded_base64_authorization_header:
            return None, None
        # split the decoded value into "{email} ':' {}password"
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Create a user object from the user credentials
        Args:
            self (_type_):
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        # search for User instance in the database (file)
        users = User.search({"email": user_email})  # list of User instances
        if not users:  # no users found wit the given email
            return None

        user = users[0]
        if not user.is_valid_password(user_pwd):  # password is not valid
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get the current user from the Flask request.
        """
        if request is None:
            return None

        # Assuming 'authorization_header' is available in the request
        authorization_header = request.get('authorization_header')
        # Extract Base64 part from Authorization header
        base64_auth_header = self.extract_base64_authorization_header(
            authorization_header)
        # Decode Base64 string
        decoded_auth_header = self.decode_base64_authorization_header(
            base64_auth_header)
        # Extract user credentials from decoded string
        user_email, user_pwd = self.extract_user_credentials(
            decoded_auth_header)
        # Get User instance based on email and password
        user = self.user_object_from_credentials(
            user_email, user_pwd)

        return user
