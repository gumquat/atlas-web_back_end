#!/usr/bin/env python3
"""description text"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """
    'Session Auth' class
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a session for the given user ID.
        Args:
            user_id (str, optional): The user ID. Defaults to None.
        Returns:
            str: The session ID.
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())  # Generate a Session ID
        # use this sessionID as key for dictionary user_id_by_session_id
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns User ID based on a Session's ID
        Args:
            session_id (str, optional): The session ID. Defaults to None.
        Returns:
            str: The User ID.
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        returns a user instance
        from a cookie or None if no cookie is set
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None
        return User.get(user_id)

    def destroy_session(self, request=None):
        """ end the session and remove the session id from the dictionary
        Args:
            request (_type_, optional): The Flask request object.
        Returns:
            nothin
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False
        del self.user_id_by_session_id[session_id]
        return True
