"""
File to create all needed fixtures to set up a Flask client
"""
import pytest
from src.app import app


@pytest.fixture()
def create_app():
    """
    This method returns an instance of an app for testing purposes
    """
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(create_app):
    """
    This methods takes an app fixture and returns a Flask http client for testing purposes
    """
    return create_app.test_client()


@pytest.fixture()
def runner(create_app):
    """
    This methods takes an app fixture and returns a Flask cli client for testing purposes
    """
    return create_app.test_cli_runner()
