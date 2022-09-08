"""
File to create all needed fixtures to set up a Flask client
"""
# pylint: disable=redefined-outer-name
import pytest
from src.app import create_app


@pytest.fixture()
def app():
    """
    This method returns an instance of an app for testing purposes
    """
    app_factory = create_app()
    app_factory.config.update(
        {
            "TESTING": True,
        }
    )

    # mock data here

    yield app_factory

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    """
    This methods takes an app fixture and returns a Flask http client for testing purposes
    """
    return app.test_client()


@pytest.fixture()
def runner(app):
    """
    This methods takes an app fixture and returns a Flask cli client for testing purposes
    """
    return app.test_cli_runner()


# pylint: enable=redefined-outer-name
