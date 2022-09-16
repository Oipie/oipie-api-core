"""
    Define the database first configuration
"""
from contextlib import contextmanager
import logging
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, orm
from src.config.db import database_url_connection


Models = declarative_base()
logger = logging.getLogger(__name__)


class Database:
    """
    Includes all methods of SqlAlquemy data implementation
    """

    def __init__(self, url_connection=database_url_connection()):
        self._engine = create_engine(url_connection)
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(bind=self._engine),
        )

    def create_database(self):
        """
        Creates all tables if not exists
        """
        Models.metadata.create_all(self._engine)

    def get_engine(self):
        """
        Returns engine
        """
        return self._engine

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
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            logger.exception("Session rollback because of exception")
            session.rollback()
            raise
        finally:
            session.close()


class TestingDatabase(Database):
    """
    Database class for testing purposes
    """

    def __init__(self):
        database_test_config = {"database_name": "oipie_tests"}
        database_test_uri = database_url_connection(database_test_config)
        super().__init__(database_test_uri)
        self._session = self._session_factory()

    def session(self):
        """
        Allow to access the database session
        """
        return self._session
