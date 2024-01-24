#!/usr/bin/env python3
""" Auth Model """
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
import uuid


class Auth:
    """class for interacting with db
    """

    def __init__(self):
        self._db = DB()

    def valid_login(self, email: str, password: str) -> bool:
        """checks for valid login
        Args:
            email and password
        Returns:
            True if login is valid
            False if login is invalid
        """
        try:  # locate the user by email again
            user = self._db.find_user_by(email=email)
            if user and bcrypt.checkpw(  # user & pword are good, return true
                    password.encode('utf-8'), user.hashed_password):
                return True
        except NoResultFound:
            pass  # nothing here yet
        except InvalidRequestError:
            pass  # nothing here yet
        return False

    def _hash_password(self, password: str) -> bytes:
        """hash password
        """
        salt = bcrypt.gensalt()  # generate random salt
        # hash the password and store it in hashed_password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password  # return the hashed password

    def register_user(self, email: str, password: str) -> User:
        """make a user with email and password
        """
        try:  # check if user already exists in db
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:  # if user does not exist, create user
            hashed_password = self._hash_password(password)  # hash password
            new_user = self._db.add_user(email, hashed_password)  # user to db
            return new_user  # return new user data

    def create_session(self, email: str) -> str:
        """Create a session ID for a user with their email.
        """
        user = self._db.find_user_by(email=email)
        if user:
            session_id = str(uuid.uuid4())
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """Return the user or None."""
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int):
        """Destroy a user session by setting the user's session ID to None.
        """
        if user_id is not None:
            try:
                self._db.update_user(user_id, session_id=None)
            except (NoResultFound, InvalidRequestError):
                pass

    def get_reset_password_token(self, email: str) -> str:
        """ If it exists, generate a UUID and update the user’s reset_token
            database field. Return the token """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        token = _generate_uuid()
        self._db.update_user(user.id, reset_token=token)
        return token

    def update_password(self, reset_token: str, password: str) -> None:
        """ hash the password and update the user’s hashed_password field with
            the new password and the reset_token field to None """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError
        pwd = _hash_password(password)
        self._db.update_user(user.id, hashed_password=pwd, reset_token=None)

# OUTSIDE THE AUTH CLASS STARTS HERE

def _hash_password(password: str) -> bytes:
    """hash password
    """
    salt = bcrypt.gensalt()  # generate random salt
    # hash the password and store it in hashed_password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password  # return the hashed password


def _generate_uuid() -> str:
    """generate a UUID then return it as a string
    """
    return str(uuid.uuid4())
