#!/usr/bin/env python3

"""DB module
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound, InvalidRequestError
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
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
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user


    def find_user_by(self, **kwargs) -> User:
        """Find a user in the database
        based on input arguments
        Args:
            Self:
            Kwargs:
        Returns:
            User:
        """
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound("No user found.")
            return user
        except InvalidRequestError as x:
            raise InvalidRequestError(f"Invalid request: {x}")
