#!/usr/bin/env python3
"""description text"""
from api.v1.auth.auth import Auth
import os


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
        else:
            session_id = str(uuid.uuid4()) # Generate a Session ID
            # Use this sessionID as key for dictionary user_id_by_session_id
            self.user_id_by_session_id[session_id] = user_id
            return session_id
