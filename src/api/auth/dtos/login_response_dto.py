"""
LoginResponseDto
"""


class LoginResponseDTO:
    """
    Class that serializes an auth token
    """

    @staticmethod
    def serialize(token: str) -> dict[str]:
        """
        Serializes token into a JSON-like dict
        """
        return {"auth_token": token}
