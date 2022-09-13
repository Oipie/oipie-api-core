"""
User module
"""
from typing import Optional, TypedDict


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
