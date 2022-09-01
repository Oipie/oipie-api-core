"""
ese
"""
from src.core.recipes.infrastructure.recipe_model import RecipeModel
from src.core.recipes.domain.recipe import Recipe


class RecipesRepositorySQLAlchemy:
    """
    This class manages database connection to query within recipes table
    """

    def find_all(self) -> list[Recipe]:
        """
        Gets all recipes from database and returns domain objects
        """
        return list(map(lambda recipie: recipie.to_domain_object(), RecipeModel.query.all()))
