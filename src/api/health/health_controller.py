"""
This module serves the purpose of checking if API is OK
"""

import http
from flask import Blueprint
from dependency_injector.wiring import Provide, inject
from sqlalchemy.sql import text
from src.config.container import Container
from src.config.session_handler import SessionHandler


health_bp = Blueprint("health_bp", __name__)

health_bp = Blueprint("health_bp", __name__)


@health_bp.route("/health", methods=["GET"])
@inject
def health(session_handler: SessionHandler = Provide[Container.session_handler]):
    """
    This routes returns a 204 No Content to check if API is alive
    """
    with session_handler.get_session() as session:
        session.execute(text("SELECT 1"))
    return "", http.HTTPStatus.NO_CONTENT
