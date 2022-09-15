"""
User repository SQLAlchemy implementation tests
"""
import pytest
from src.core.users.infrastructure.user_repository_sqlalchemy import UsersRepositorySQLAlchemy
from src.core.users.infrastructure.user_model import UserModel
from src.tests.fixtures.user_fixture import JOHN

# pylint: disable=redefined-outer-name, unused-argument


@pytest.fixture()
def users_repository(database_instance):
    """
    Creates a UserRepositorySQLAlchemy instance with session
    """

    return UsersRepositorySQLAlchemy(database_instance.session)


@pytest.fixture()
def create_john_user(session):
    """
    Creates user from JOHN fixture
    """
    john_model = UserModel(
        uuid=JOHN["uuid"], nickname=JOHN["nickname"], email=JOHN["email"], password=JOHN["password"]
    )

    session.add(john_model)
    session.flush()


def test_find_by_email_not_finds_client(users_repository: UsersRepositorySQLAlchemy):
    """
    Checks user is not found if email does not exist in repository
    """
    email = JOHN["email"]

    user = users_repository.find_by_email(email)

    assert user is None


def test_find_by_email_finds_client(users_repository: UsersRepositorySQLAlchemy, create_john_user):
    """
    Checks user is found if email exists in repository
    """
    email = JOHN["email"]

    user = users_repository.find_by_email(email)

    assert user is not None
    serialized_user = user.serialize()
    assert serialized_user["email"] == email


# pylint: enable=redefined-outer-name, unused-argument
