from typing import List
from typing import TypeVar
from flask import request


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if authentication is required for the given path.
        Args:
        - path (str): The path to check for authentication requirement.
        - excluded_paths (List[str]): List of paths to be excluded from authentication.
        Returns:
        - bool: True if authentication is required, False otherwise.
        """
        return False


    def authorization_header(self, request=None) -> str:
        """
        Get the Authorization header from the Flask request.
        Args:
        - request: The Flask request object.
        Returns:
        - str: The Authorization header or None.
        """
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """
        Get the current user from the Flask request.
        Args:
        - request: The Flask request object.
        Returns:
        - TypeVar('User'): The current user or None.
        """
        return None
