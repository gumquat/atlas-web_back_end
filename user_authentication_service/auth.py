#!/usr/bin/env python3
""" auth model """

import bcrypt
from db import DB
from user import User
import uuid
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


class Auth:
    """allows for user authentication and working with the database of users
    """

    def __init__(self):
        self._db = DB()

    def _hash_password(password: str) -> bytes:
        """hash password
        """
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
