"""
    Domain recipes repository interface module
"""
import abc
from typing import Tuple
from src.core.recipes.domain.recipe import Recipe


class RecipesRepository(abc.ABC):
    """
    Domain recipes repository interface
    """
    @abc.abstractmethod
    def find_all(self, offset: int, limit: int) -> Tuple[list[Recipe], int]:
        """
            Find all recipes on database.
        """
        raise NotImplementedError
