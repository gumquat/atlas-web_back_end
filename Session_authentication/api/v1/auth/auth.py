#!/usr/bin/env python3
"""documentation string here"""
from flask import request
from typing import List, TypeVar


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
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
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
