"""
This module handlers all exceptions regarding HTTP error codes
"""

from flask import json, Blueprint
from werkzeug.exceptions import HTTPException

errors_bp = Blueprint('errors', __name__)


@errors_bp.app_errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response