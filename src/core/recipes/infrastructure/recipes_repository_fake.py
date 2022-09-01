"""
ese
"""
from src.core.recipes.domain.recipes_repository import RecipesRepository
from src.core.recipes.domain.recipe import Recipe


class RecipesRepositoryFake(RecipesRepository):
    """
    This class manages database connection to query within recipes table
    """

    def __init__(self, recipes):
        self.recipes = recipes

    def find_all(self) -> list[Recipe]:
        """
        Gets all recipes from database and returns domain objects
        """
        return list(self.recipes)
