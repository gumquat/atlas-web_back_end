#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """adds new user to db
        Args:
            email (str): user email
            hashed_password (str): user pword
        Returns:
            User: user as an object
        """
        DBSession = sessionmaker(bind=self._engine)

        session = DBSession()  # Open a new session
        new_user = User(email=email, hashed_password=hashed_password)
        session.add(new_user)
        session.commit()

        session.close()  # Close the session
        return new_user
