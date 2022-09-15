"""
SQLAlchemy repository for Users
"""
from typing import Callable
from contextlib import AbstractContextManager
from sqlalchemy.orm import Session
from src.core.users.domain.user import User
from src.core.users.domain.users_repository import UsersRepository
from src.core.users.infrastructure.user_model import UserModel


class UsersRepositorySQLAlchemy(UsersRepository):
    """
    This class manages database connection to query within users table
    """

    model = UserModel

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session = session_factory

    def find_by_email(self, email: str) -> User or None:
        with self.session() as session:
            user_model = session.query(self.model).filter_by(email=email).one_or_none()
            if user_model is None:
                return None

            return user_model.to_domain_object()
