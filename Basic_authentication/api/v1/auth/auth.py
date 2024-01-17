#!/usr/bin/env python3

""" Create a class to manage an API authenication """

from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class for API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for the given path"""
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        normal_path = path if path.endswith("/") else path + "/"
        for excluded_path in excluded_paths:
            if excluded_path.endswith("/"):
                if normal_path == excluded_path:
                    return False
            else:
                if path.startswith(excluded_path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """Get the Authorization header from the request"""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current user from the request"""
        return None
