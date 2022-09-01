"""
PaginatedResponseDTO
"""


class PaginatedResponseDTO:
    """
    This class is responsible to, given a object list, serialize it in a JSON-format dict
    """

    @staticmethod
    def serialize(object_list: list, total_objects: int) -> dict:
        """
        This method returns JSON-format dict within the object_list metadata
        """
        return {
            'items': object_list,
            'meta': {
                'totalItems': total_objects
            }
        }
