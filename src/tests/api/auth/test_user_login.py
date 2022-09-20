"""
Tests to check /register (POST) endpoint
"""
from src.tests.fixtures.user_fixture import JOHN


def test_user_login_successfully(api_client):
    """
    This test checks that an user is registered successfully
    """

    api_client.register_user(
        email=JOHN["email"], nickname=JOHN["nickname"], password=JOHN["password"]
    )
    api_client.authenticate_user(email=JOHN["email"], password=JOHN["password"])
