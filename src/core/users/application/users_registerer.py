"""
Users Registerer use case
"""
from src.core.users.domain.errors.user_with_email_already_exists_error import (
    UserWithEmailAlreadyExistsError,
)
from src.core.users.domain.errors.user_with_nickname_already_exists_error import (
    UserWithNicknameAlreadyExistsError,
)
from src.core.users.domain.user import User
from src.core.users.domain.users_repository import UsersRepository


class UsersRegisterer:
    """
    This class returns a list of recipies
    """

    def __init__(self, users_repository: UsersRepository):
        self.users_repository = users_repository

    def execute(self, nickname: str, email: str, password: str) -> None:
        """
        Creates a user if their nickname nor email exist in database
        """
        user_with_email = self.users_repository.find_by_email(email)
        if user_with_email is not None:
            raise UserWithEmailAlreadyExistsError(email)

        user_with_nickname = self.users_repository.find_by_nickname(nickname)
        if user_with_nickname is not None:
            raise UserWithNicknameAlreadyExistsError(nickname)

        new_user = User.create(nickname, email, password)
        self.users_repository.create(new_user)
