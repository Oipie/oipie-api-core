"""
Recipies Lister use case
"""
from src.core.recipes.domain.recipe import Recipe
from src.core.recipes.infrastructure.recipes_repository_sqlalchemy import RecipesRepositorySQLAlchemy


class RecipiesLister:
    """
    This class returns a list of recipies
    """

    def __init__(self):
        self.recipes_repository = RecipesRepositorySQLAlchemy()

    def execute(self) -> list[Recipe]:
        """
        Returns a list of recipies
        """
        return self.recipes_repository.find_all()
