#!/usr/bin/env python3
"""description text"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """
    'Session Auth' class
    """

    user_id_by_seession_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a session for the given user ID.
        Args:
            user_id (str, optional): The user ID. Defaults to None.
        Returns:
            str: The session ID.
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4()) # Generate a Session ID
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
        if session_id is None or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)
