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
