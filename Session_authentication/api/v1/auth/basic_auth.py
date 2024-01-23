#!/usr/bin/env python3
"""We will update this later"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """Empty Basic auth class"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns the Base64 part of the Authorization
        header for a Basic Authentication"""
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
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
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        user_email, user_password =\
            decoded_base64_authorization_header.split(':', 1)
        return user_email, user_password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Create a user object from the user credentials
        Args:
            self (_type_):
        """
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

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
