"""
Tests to check /register (POST) endpoint
"""
from http import HTTPStatus
import json
from src.tests.fixtures.user_fixture import JOHN, JANE


def test_user_is_registered(client):
    """
    This test checks that an user is registered successfully
    """

    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}
    data = {
        "nickname": JOHN["nickname"],
        "email": JOHN["email"],
        "password": JOHN["password"],
    }

    response = client.post("register", data=json.dumps(data), headers=headers)

    assert response.status_code == HTTPStatus.CREATED


def test_user_register_fails_if_already_existing(client):
    """
    This test checks that an user is registered successfully
    """

    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}
    data = {
        "nickname": JANE["nickname"],
        "email": JANE["email"],
        "password": JANE["password"],
    }

    response = client.post("register", data=json.dumps(data), headers=headers)
    register_response = client.post("register", data=json.dumps(data), headers=headers)

    assert response.status_code == HTTPStatus.CREATED
    assert register_response.status_code == HTTPStatus.CONFLICT
