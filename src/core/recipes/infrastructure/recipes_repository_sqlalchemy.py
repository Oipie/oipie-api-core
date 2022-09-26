"""
SQLAlchemy repository for Recipes
"""
from src.config.session_handler import SessionHandler
from src.core.recipes.domain.recipes_repository import RecipesRepository
from src.core.recipes.infrastructure.recipe_model import RecipeModel
from src.core.recipes.domain.recipe import Recipe


class RecipesRepositorySQLAlchemy(RecipesRepository):
    """
    This class manages database connection to query within recipes table
    """

    model = RecipeModel

    def __init__(self, session_handler: SessionHandler):
        self.session = session_handler.get_session()

    def find_all(self, offset: int, limit: int) -> tuple[list[Recipe], int]:
        """
        Gets all recipes from database and returns domain objects
        """
        query = self.session.query(RecipeModel)
        count: int = query.count()
        return (
            list(
                map(
                    lambda recipie: recipie.to_domain_object(),
                    query.limit(limit).offset(offset).all(),
                )
            ),
            count,
        )
