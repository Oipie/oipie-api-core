"""
User module
"""
from typing import Optional, TypedDict
from uuid import uuid4


class UserAttributes(TypedDict):
    """
    Dictionary that represents an user attributes
    """

    id_: Optional[int]
    uuid: str
    nickname: str
    email: str
    password: str


class User:
    """
    Class to modelate a domain User
    """

    def __init__(self, user_attributes: UserAttributes) -> None:
        self.id_ = user_attributes.get("id_")
        self.uuid = user_attributes.get("uuid")
        self.nickname = user_attributes.get("nickname")
        self.email = user_attributes.get("email")
        self.password = user_attributes.get("password")

    @staticmethod
    def create(nickname: str, email: str, password: str):
        """
        Creates a new user with a new uuid
        """
        return User(
            user_attributes={
                "uuid": uuid4(),
                "nickname": nickname,
                "email": email,
                "password": password,
            }
        )

    def serialize(self) -> UserAttributes:
        """
        This method returns a user parsed to dict object
        """
        user_serialized: UserAttributes = {
            "id_": self.id_,
            "uuid": self.uuid,
            "nickname": self.nickname,
            "email": self.email,
        }

        return user_serialized

    def to_payload(self) -> dict:
        """
        Returns an user to payload-based dict useful for encode user's information into a JWT
        """
        return {"email": self.email, "nickname": self.nickname}
