"""
User Database Model
"""
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String
from src.config.database_handler import Models
from src.core.users.domain.user import User


class UserModel(Models):
    """
    This class represents a User in database model
    """

    __tablename__ = "users"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    nickname = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    @staticmethod
    def from_domain_object(user: User):
        """
        Transforms to User model
        """
        return UserModel(
            uuid=user.uuid,
            nickname=user.nickname,
            email=user.email,
            password=user.password,
        )

    def to_domain_object(self) -> User:
        """
        Transforms User database model to a domain object
        """
        return User(
            {
                "uuid": self.uuid,
                "nickname": self.nickname,
                "email": self.email,
                "password": self.password,
            }
        )
