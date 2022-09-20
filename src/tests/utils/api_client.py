"""
ApiClient
"""
from http import HTTPStatus
import json
from src.tests.fixtures.user_fixture import JOHN


class ApiClient:
    """
    Class to provide each endpoint interaction for testing purposes
    """

    def __init__(self, client) -> None:
        self._client = client

    def get_recipes(self, limit=10, offset=0):
        """
        GET /recipes endpoint
        """
        query_parameters = {"limit": limit, "offset": offset}
        response = self._client.get("/recipes", query_string=query_parameters)

        assert response.status_code == HTTPStatus.OK

        return response.json

    def register_user(
        self,
        nickname=JOHN["nickname"],
        email=JOHN["email"],
        password=JOHN["password"],
        expected_status=HTTPStatus.CREATED,
    ):
        """
        POST /register endpoint
        """
        mimetype = "application/json"
        headers = {"Content-Type": mimetype, "Accept": mimetype}
        data = {
            "nickname": nickname,
            "email": email,
            "password": password,
        }
        response = self._client.post("register", data=json.dumps(data), headers=headers)

        assert response.status_code == expected_status

        return response.json

    def authenticate_user(self, email=JOHN["email"], password=JOHN["password"]):
        """
        POST /login endpoint
        """
        mimetype = "application/json"
        headers = {"Content-Type": mimetype, "Accept": mimetype}
        data = {
            "email": email,
            "password": password,
        }
        response = self._client.post("login", data=json.dumps(data), headers=headers)

        assert response.status_code == HTTPStatus.OK

        return response.json
