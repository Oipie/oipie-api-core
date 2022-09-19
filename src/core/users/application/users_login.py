"""
Users Login use case
"""
from src.core.users.domain.errors.user_credentials_error import (
    UserCredentialsError,
)
from src.core.users.domain.users_repository import UsersRepository
from src.shared.services.password.password import Password


class UsersLogin:
    """
    This class executes the flow to authenticate an user
    """

    def __init__(self, users_repository: UsersRepository, password_hasher: Password):
        self.users_repository = users_repository
        self.password_hasher = password_hasher

    def execute(self, email: str, password: str) -> None:
        """
        Creates a user if their nickname nor email exist in database
        """
        user_with_email = self.users_repository.find_by_email(email)
        if user_with_email is None:
            raise UserCredentialsError

        if not self.password_hasher.verify(user_with_email.password, password):
            raise UserCredentialsError
