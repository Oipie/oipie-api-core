"""
    Domain users repository interface module
"""
import abc
from src.core.users.domain.user import User


class UsersRepository(abc.ABC):
    """
    Domain users repository interface
    """

    @abc.abstractmethod
    def find_by_email(self, email: str) -> User or None:
        """
        Find user on database by email
        """
        raise NotImplementedError
