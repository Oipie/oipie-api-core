"""
UserWithEmailAlreadyExistsError
"""


class UserWithEmailAlreadyExistsError(Exception):
    """
    Exception raised when a user with a specific email already exists in repository
    """

    def __init__(self, email) -> None:
        super().__init__(f"Email {email} already exists in repository")
