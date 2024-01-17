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
    pass
