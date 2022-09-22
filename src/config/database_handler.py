"""
    Define the database first configuration
"""
import logging
from sqlalchemy.engine import Connection
from sqlalchemy.ext.declarative import declarative_base


Models = declarative_base()
logger = logging.getLogger(__name__)


class DatabaseHandler:
    """
    Includes all methods of SqlAlquemy data implementation
    """

    def __init__(self, connection: Connection):
        self._connection = connection

    def get_engine(self):
        """
        Returns the engine
        """
        return self._connection.engine

    def get_metadata(self):
        """
        Returns the metadata
        """
        return Models.metadata

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
