"""
    Define the database first configuration
"""
from contextlib import contextmanager
import logging
from typing import overload
from sqlalchemy.orm import Session
from sqlalchemy.engine import Connection
from sqlalchemy.ext.declarative import declarative_base
from src.config.db import database_url_connection


Models = declarative_base()
logger = logging.getLogger(__name__)


class Database:
    """
    Includes all methods of SqlAlquemy data implementation
    """

    def __init__(self, connection: Connection):
        self._connection = connection
        self._session = Session(
            bind=self._connection,
        )
        self._session.begin()

    def __del__(self):
        print("Closing database connection")
        try:
            self._session.commit()
        except:
            self._session.rollback()
            raise
        finally:
            self._session.close()

    def create_database(self):
        """
        Creates all tables if not exists
        """
        Models.metadata.create_all(self._connection)

    def get_engine(self):
        """
        Returns engine
        """
        return self._connection.engine

    def get_metadata(self):
        """
        Returns database metadata
        """
        return Models.metadata

    @contextmanager
    def session(self):
        """
        Allow to access the database session
        """
        try:
            yield self._session
        except Exception:
            self._session.rollback()
            raise


class TestingDatabase(Database):
    """
    Database class for testing purposes
    """

    def __init__(self, connection: Connection):
        self._connection = connection
        self._session = Session(
            bind=self._connection,
        )
        self._session.begin()

    def __init__2(self):
        database_test_config = {"database_name": "oipie_tests"}
        database_test_uri = database_url_connection(database_test_config)
        super().__init__(database_test_uri)
        self._session = self._session_factory()

    # def session(self):
    #     """
    #     Allow to access the database session
    #     """
    #     return self._session

    # @overload
    # @contextmanager
    # def session(self):
    #     """
    #     Allow to access the database session
    #     """
    #     session: Session = self._session_factory()
    #     try:
    #         session.begin()
    #         yield session
    #     except:
    #         logger.exception("Session rollback because of exception")
    #         raise
    #     finally:
    #         session.rollback()
    #         session.close()
