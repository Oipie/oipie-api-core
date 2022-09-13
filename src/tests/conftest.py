"""
File to create all needed fixtures to set up a Flask client
"""
# pylint: disable=redefined-outer-name, unused-argument
import pytest
from sqlalchemy.orm import sessionmaker
from dependency_injector import providers
from src.app import create_app
from src.config.container import Container
from src.config.database import TestingDatabase
from src.config.db import database_url_connection

database = TestingDatabase()
engine = database.get_engine()
Session = sessionmaker()
container = Container()


@pytest.fixture(scope="module")
def connection():
    """
    Manages database connection
    """
    connection = engine.connect()
    yield connection
    connection.close()


@pytest.fixture(scope="function")
def session(connection):
    """
    Manages database session and rollsback executed queries
    """
    transaction = connection.begin()
    session = Session(bind=connection)
    yield session
    session.close()
    transaction.rollback()


@pytest.fixture(scope="session", autouse=True)
def initialise_db():
    """
    Migrates the database once before running tests
    """
    database.create_database()


@pytest.fixture()
def create_test_app(session):
    """
    This method returns an instance of an app for testing purposes
    """
    database_test_config = {"database_name": "oipie_tests"}
    database_test_uri = database_url_connection(database_test_config)
    app_factory = create_app()
    app_factory.config.update({"TESTING": True, "SQLALCHEMY_DATABASE_URI": database_test_uri})
    app_factory.container.db.override(providers.Singleton(TestingDatabase))

    # other setup can go here

    yield app_factory

    # clean up / reset resources here


@pytest.fixture()
def client(create_test_app):
    """
    This methods takes an app fixture and returns a Flask http client for testing purposes
    """
    return create_test_app.test_client()


@pytest.fixture()
def runner(create_test_app):
    """
    This methods takes an app fixture and returns a Flask cli client for testing purposes
    """
    return create_test_app.test_cli_runner()


# pylint: enable=redefined-outer-name, unused-argument
