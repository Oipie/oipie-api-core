"""
ese
"""
from typing import Tuple
from src.core.recipes.domain.recipes_repository import RecipesRepository
from src.core.recipes.infrastructure.recipe_model import RecipeModel
from src.core.recipes.domain.recipe import Recipe


class RecipesRepositorySQLAlchemy(RecipesRepository):
    """
    This class manages database connection to query within recipes table
    """

    def __init__(self, session):
        self.session = session

    def find_all(self, offset: int, limit: int) -> Tuple[list[Recipe], int]:
        """
        Gets all recipes from database and returns domain objects
        """
        query = self.session.query(RecipeModel)
        count: int = query.count()

        return (list(map(lambda recipie: recipie.to_domain_object(),
                         query.limit(limit).offset(offset).all())), count)
