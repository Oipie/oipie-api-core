"""
UserWithNicknameAlreadyExistsError
"""


class UserWithNicknameAlreadyExistsError(Exception):
    """
    Exception raised when a user with a specific nickname already exists in repository
    """

    def __init__(self, nickname) -> None:
        super().__init__(f"Nickname {nickname} already exists in repository")
