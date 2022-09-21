"""
This module serves the purpose of perform several actions on the recipes
"""

from dependency_injector.wiring import Provide, inject
from flask import Blueprint, request, Response
from src.config.container import Container
from src.core.users.application.users_registerer import UsersRegisterer
from src.api.auth.dtos.login_response_dto import LoginResponseDTO


auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.route("/register", methods=["POST"])
@inject
def register(users_registerer: UsersRegisterer = Provide[Container.users_registerer]):
    """
    This route returns a 201 CREATED if user is successfully registered
    """
    if request.is_json:
        data = request.get_json(force=True)
        users_registerer.execute(data["nickname"], data["email"], data["password"])
        return Response(status=201)

    return Response(status=400)


@auth_bp.route("/login", methods=["POST"])
@inject
def login(users_login: UsersRegisterer = Provide[Container.users_login]):
    """
    This route returns a 200 OK with the auth token user's credentials are successful
    """
    # raise Exception("SENKIU")
    if request.is_json:
        data = request.get_json(force=True)
        auth_token = users_login.execute(data["email"], data["password"])

        return LoginResponseDTO.serialize(auth_token)

    return Response(status=400)
