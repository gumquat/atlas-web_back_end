#!/usr/bin/env python3

"""documentation string here"""

from typing import List
from typing import TypeVar
from flask import request
import os


class Auth:
    """auth class for the API"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for the given path.
        Args:
        - path (str): The path to check for authentication requirement.
        - excluded_paths (List[str]): List of paths to be excluded
        from authentication.
        Returns:
        - bool: True if authentication is required, False otherwise.
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        # Check for trailing slash, if none found, add it.
        if path.endswith("/"):
            normal_path = path
        else:
            normal_path = path + "/"

        for excluded_path in excluded_paths:  # Checking for an exact match.
            if excluded_path.endswith("/"):  # check for trailing slash
                if normal_path == excluded_path:  # exact match is found here
                    return False  # return false if exact match found
            else:
                if path.startswith(excluded_path):  # Check for prefix.
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """Get the Authorization header from the Flask request.
        Args:
        - request: The Flask request object.
        Returns:
        - str: The Authorization header or None.
        """
        # Check if the header exists.
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']  # Return the header.

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current user from the Flask request.
        Args:
        - request: The Flask request object.
        Returns:
        - TypeVar('User'): The current user or None.
        """

    def session_cookie(self, request=None):
        """_summary_
        Args:
            request (_type_, optional): _description_. Defaults to None.
        Returns:
            _type_: return cookie value from a request
        """
        if request is None:
            return None
        return request.cookies.get(os.getenv('SESSION_NAME'))
