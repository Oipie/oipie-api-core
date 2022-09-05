"""
File to create all needed fixtures to set up a Flask client
"""
# pylint: disable=redefined-outer-name, unused-argument
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.app import create_app
from src.config.db import database_url_connection

database_test_config = {
    'database_name': 'oipie_tests'
}
database_test_uri = database_url_connection(database_test_config)
engine = create_engine(database_test_uri)
Session = sessionmaker()


@pytest.fixture(scope='module')
def connection():
    """
    Manages database connection
    """
    connection = engine.connect()
    yield connection
    connection.close()


@pytest.fixture()
def create_test_app(connection):
    """
    This method returns an instance of an app for testing purposes
    """
    app_factory = create_app()
    app_factory.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": database_test_uri
    })

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
