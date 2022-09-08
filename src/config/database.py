"""
    Define the database first configuration
"""
from contextlib import contextmanager, AbstractContextManager
from typing import Callable
import logging
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, orm, MetaData
from src.config.db import DATABASE_URL_CONECTION

Models = declarative_base()
logger = logging.getLogger(__name__)


class Database:
    """
    Includes all methods of SqlAlquemy data implementation
    """

    def __init__(self):
        self._engine = create_engine(DATABASE_URL_CONECTION, echo=False)
        self._metadata = MetaData(bind=self._engine)
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            ),
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
        return self._metadata

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
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
