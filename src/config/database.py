"""
    Define the database first configuration
"""
from contextlib import contextmanager
import logging
from sqlalchemy.orm import Session
from sqlalchemy.engine import Connection
from sqlalchemy.ext.declarative import declarative_base


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
        try:
            self._session.commit()
        except:
            self._session.rollback()
            raise
        finally:
            self._session.close()

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

    def __del__(self):
        pass

    def create_database(self):
        """
        Creates all tables if not exists
        """
        Models.metadata.create_all(self._connection)

    def drop_database(self):
        """
        Drops all tables
        """
        Models.metadata.drop_all(self._connection)
