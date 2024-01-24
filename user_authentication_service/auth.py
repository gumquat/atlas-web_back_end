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

    def _hash_password(self, password: str) -> bytes:
        """hashes user passwords
        wit hsalt so they can be stored gooder
        """
        salt = bcrypt.gensalt()  # generate random salt
        # hash the password and store it in hashed_password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password  # return the hashed password
