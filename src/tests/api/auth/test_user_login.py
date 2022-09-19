"""
Tests to check /register (POST) endpoint
"""
from http import HTTPStatus
import json
from src.tests.fixtures.user_fixture import JOHN


def test_user_login_successfully(client):
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
    login_response = client.post("login", data=json.dumps(data), headers=headers)

    assert response.status_code == HTTPStatus.CREATED
    assert login_response.status_code == HTTPStatus.OK
