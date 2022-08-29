"""
This module serves the purpose of checking if API is OK
"""

import http
from flask import Blueprint
from sqlalchemy.sql import text
from src.app import db

health_bp = Blueprint('health_bp', __name__)


@health_bp.route("/health", methods=['GET'])
def health():
    """
    This routes returns a 204 No Content to check if API is alive
    """
    db.session().execute(text('SELECT 1'))
    return '', http.HTTPStatus.NO_CONTENT
