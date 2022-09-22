"""
File to create all needed fixtures to set up a Flask client
"""
# pylint: disable=redefined-outer-name, unused-argument
from typing import Generator
import pytest
from sqlalchemy import create_engine
from sqlalchemy.engine import Connection
from dependency_injector import providers
from src.app import create_app
from src.config.container import Container
from src.config.database_handler import DatabaseHandler
from src.config.db import database_url_connection
from src.config.session_handler import SessionHandler
from src.tests.utils.api_client import ApiClient

container = Container()


@pytest.fixture(scope="session")
def connection() -> Generator[Connection, None, None]:
    """
    Manages database connection
    """
    _engine = create_engine(url=database_url_connection({"database_name": "oipie_tests"}))
    _connection = _engine.connect()
    yield _connection
    _connection.close()


@pytest.fixture(scope="session", autouse=True)
def initialise_db(connection: Connection):
    """
    Migrates the database once before running tests
    """
    _database = DatabaseHandler(connection)
    _database.create_database()
    yield
    _database.drop_database()


@pytest.fixture(autouse=True)
def transaction(connection: Connection):
    """
    Wraps the test in a transaction
    """
    _transaction = connection.begin()
    yield
    _transaction.rollback()


@pytest.fixture()
def session_handler(connection):
    """
    Creates a session handler
    """
    return SessionHandler(connection)


@pytest.fixture()
def create_test_app():
    """
    This method returns an instance of an app for testing purposes
    """
    app_factory = create_app()
    app_factory.container.connection.override(providers.Object(connection))

    # other setup can go here

    yield app_factory

    # clean up / reset resources here


@pytest.fixture()
def client(create_test_app):
    """
    This methods takes an app fixture and returns a Flask http client for testing purposes
    """
    return create_test_app.test_client()


# @pytest.fixture()
# def runner(create_test_app):
#     """
#     This methods takes an app fixture and returns a Flask cli client for testing purposes
#     """
#     return create_test_app.test_cli_runner()


@pytest.fixture()
def api_client(client):
    """
    Generates an API Client
    """
    return ApiClient(client)


# pylint: enable=redefined-outer-name, unused-argument
