"""
UsersLogin tests
"""
import pytest
from src.core.users.application.users_login import UsersLogin
from src.core.users.domain.errors.user_credentials_error import (
    UserCredentialsError,
)
from src.core.users.domain.user import User
from src.core.users.infrastructure.user_repository_fake import UsersRepositoryFake
from src.shared.services.password.plain_text_password import PlainTextPassword
from src.tests.fixtures.user_fixture import JANE, JOHN

# pylint: disable=redefined-outer-name


@pytest.fixture(scope="module")
def password_hasher():
    """
    Fixture to not compute hard passwords when registering users in use case
    """
    return PlainTextPassword()


def test_user_not_found_raises_credentials_error(password_hasher):
    """
    Checks user not found in repository by email raises UserCredentialsError
    """
    users_repository = UsersRepositoryFake()
    users_registerer = UsersLogin(users_repository, password_hasher)

    with pytest.raises(UserCredentialsError):
        users_registerer.execute(JOHN["email"], JOHN["password"])


def test_user_password_not_matches_raises_credentials_error(password_hasher):
    """
    Checks password hasher fails if password does not match user's found in repository
    """
    existing_user = User.create(
        nickname=JANE["nickname"], email=JOHN["email"], password=JOHN["password"]
    )
    users_repository = UsersRepositoryFake(users=[existing_user])
    users_registerer = UsersLogin(users_repository, password_hasher)

    with pytest.raises(UserCredentialsError):
        users_registerer.execute(JOHN["email"], JANE["password"])


# pylint: enable=redefined-outer-name
