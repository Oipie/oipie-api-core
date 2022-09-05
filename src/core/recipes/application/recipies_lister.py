"""
Recipies Lister use case
"""
from typing import Tuple
from src.core.recipes.domain.recipe import Recipe
from src.core.recipes.domain.recipes_repository import RecipesRepository


class RecipiesLister:
    """
    This class returns a list of recipies
    """

    def __init__(self, recipes_repository: RecipesRepository):
        self.recipes_repository = recipes_repository

    def execute(self, offset: int, limit: int) -> Tuple[list[Recipe], int]:
        """
        Returns a list of recipies
        """
        return self.recipes_repository.find_all(offset, limit)
