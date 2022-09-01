"""
ese
"""
from src.core.recipes.domain.recipes_repository import RecipesRepository
from src.core.recipes.infrastructure.recipe_model import RecipeModel
from src.core.recipes.domain.recipe import Recipe


class RecipesRepositorySQLAlchemy(RecipesRepository):
    """
    This class manages database connection to query within recipes table
    """

    def __init__(self, session):
        self.session = session

    def find_all(self) -> list[Recipe]:
        """
        Gets all recipes from database and returns domain objects
        """
        return list(map(lambda recipie: recipie.to_domain_object(),
                        self.session.query(RecipeModel).all()))
