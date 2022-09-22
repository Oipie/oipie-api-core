"""
InvalidTokenError
"""
from src.core.shared.domain.base_exception import DomainException, ExceptionCategory


class InvalidTokenError(DomainException):
    """
    Exception to manage invalid token exceptions, ie: a token has expired
    """

    def __init__(self, *args: object) -> None:
        super().__init__("Token is not valid", "INVALID_TOKEN", ExceptionCategory.CONFLICT, *args)
