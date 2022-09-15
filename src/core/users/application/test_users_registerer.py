"""
UsersRegisterer tests
"""
import pytest
from src.core.users.application.users_registerer import UsersRegisterer
from src.core.users.domain.errors.user_with_email_already_exists_error import (
    UserWithEmailAlreadyExistsError,
)
from src.core.users.domain.errors.user_with_nickname_already_exists_error import (
    UserWithNicknameAlreadyExistsError,
)
from src.core.users.domain.user import User
from src.core.users.infrastructure.user_repository_fake import UsersRepositoryFake
from src.tests.fixtures.user_fixture import JANE, JOHN


def test_new_user_is_registered():
    """
    Checks user is successfully registered by not raising an error
    """
    users_repository = UsersRepositoryFake()
    users_registerer = UsersRegisterer(users_repository)

    users_registerer.execute(JOHN["nickname"], JOHN["email"], JOHN["password"])


def test_registerer_raises_user_with_email_error():
    """
    Checks user is successfully registered by not raising an error
    """
    existing_user = User.create(
        nickname=JANE["nickname"], email=JOHN["email"], password=JOHN["password"]
    )
    users_repository = UsersRepositoryFake(users=[existing_user])
    users_registerer = UsersRegisterer(users_repository)

    with pytest.raises(UserWithEmailAlreadyExistsError):
        users_registerer.execute(JOHN["nickname"], JOHN["email"], JOHN["password"])


def test_registerer_raises_user_with_nickname_error():
    """
    Checks user is successfully registered by not raising an error
    """
    existing_user = User.create(
        nickname=JOHN["nickname"], email=JANE["email"], password=JOHN["password"]
    )
    users_repository = UsersRepositoryFake(users=[existing_user])
    users_registerer = UsersRegisterer(users_repository)

    with pytest.raises(UserWithNicknameAlreadyExistsError):
        users_registerer.execute(JOHN["nickname"], JOHN["email"], JOHN["password"])
