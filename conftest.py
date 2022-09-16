"""
File to create all needed fixtures to set up a Flask client
"""
# pylint: disable=redefined-outer-name, unused-argument
import pytest
from sqlalchemy import create_engine
from sqlalchemy.engine import Connection, Engine
from dependency_injector import providers
from src.app import create_app
from src.config.container import Container
from src.config.database import TestingDatabase
from src.config.db import database_url_connection

container = Container()


@pytest.fixture(scope="session")
def engine():
    """
    Creates engine for testing
    """
    return create_engine(url=database_url_connection({"database_name": "oipie_tests"}))


@pytest.fixture(scope="session")
def connection(engine: Engine):
    """
    Manages database connection
    """
    connection = engine.connect()
    yield connection
    connection.close()


@pytest.fixture(scope="session")
def database(connection: Connection):
    """
    Returns database fake instance
    """
    return TestingDatabase(connection)


@pytest.fixture(scope="session", autouse=True)
def initialise_db(database: TestingDatabase):
    """
    Migrates the database once before running tests
    """
    database.create_database()
    yield
    database.drop_database()


@pytest.fixture(scope="function")
def session(database: TestingDatabase):
    """
    Manages database session and rollsback executed queries
    """
    with database.session() as session:
        nested = session.begin_nested()
        yield session
        nested.rollback()
        session.close()


@pytest.fixture()
def create_test_app(database: TestingDatabase):
    """
    This method returns an instance of an app for testing purposes
    """
    app_factory = create_app()
    app_factory.container.db.override(providers.Object(database))

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


# pylint: enable=redefined-outer-name, unused-argument
