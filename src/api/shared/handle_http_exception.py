"""
This module handlers all exceptions regarding HTTP error codes
"""

from http import HTTPStatus
from flask import json, Blueprint, jsonify, make_response
from werkzeug.exceptions import HTTPException
from src.core.shared.domain.base_exception import DomainException, ExceptionCategory

errors_bp = Blueprint("errors", __name__)


@errors_bp.app_errorhandler(HTTPException)
def handle_exception(error):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = error.get_response()
    # replace the body with JSON
    response.data = json.dumps(
        {
            "code": error.code,
            "name": error.name,
            "description": error.description,
        }
    )
    response.content_type = "application/json"
    return response


DOMAIN_CATEGORY_EXCEPTIONS_TO_HTTP: dict[ExceptionCategory, HTTPStatus] = {
    ExceptionCategory.CONFLICT: HTTPStatus.CONFLICT,
    ExceptionCategory.BAD_REQUEST: HTTPStatus.BAD_REQUEST,
    ExceptionCategory.NOT_FOUND: HTTPStatus.NOT_FOUND,
    ExceptionCategory.UNKNOWN: HTTPStatus.INTERNAL_SERVER_ERROR,
}


@errors_bp.app_errorhandler(DomainException)
def handle_domain_exception(error: DomainException):
    """Handle domain errors and return them in a JSON format"""

    return make_response(
        jsonify(
            {
                "code": error.code,
                "description": error.message,
            }
        ),
        DOMAIN_CATEGORY_EXCEPTIONS_TO_HTTP[error.category],
    )


@errors_bp.app_errorhandler(Exception)
def handle_uknown_exception(*args):
    """Handle unknown errors and return them in a JSON format"""

    print(*args)
    return make_response(
        jsonify(
            {
                "code": "UKNOWN_ERROR",
                "description": "Something has happened!",
            }
        ),
        DOMAIN_CATEGORY_EXCEPTIONS_TO_HTTP[ExceptionCategory.UNKNOWN],
    )
