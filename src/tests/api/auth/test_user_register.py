"""
Tests to check /register (POST) endpoint
"""
from http import HTTPStatus
from src.tests.fixtures.user_fixture import JANE


def test_user_is_registered(api_client):
    """
    This test checks that an user is registered successfully
    """

    api_client.register_user()


def test_user_register_fails_if_already_existing(api_client):
    """
    This test checks that an user fails if trying to register the same user twice
    """

    api_client.register_user(
        email=JANE["email"], nickname=JANE["nickname"], expected_status=HTTPStatus.CREATED
    )
    api_client.register_user(
        email=JANE["email"], nickname=JANE["nickname"], expected_status=HTTPStatus.CONFLICT
    )
