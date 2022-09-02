"""
ese
"""
from contextlib import AbstractContextManager
from typing import Callable
from sqlalchemy.orm import Session
from src.core.recipes.domain.recipes_repository import RecipesRepository
from src.core.recipes.infrastructure.recipe_model import RecipeModel
from src.core.recipes.domain.recipe import Recipe


class RecipesRepositorySQLAlchemy(RecipesRepository):
    """
    This class manages database connection to query within recipes table
    """
    model = RecipeModel

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session = session_factory

    def find_all(self) -> list[Recipe]:
        """
        Gets all recipes from database and returns domain objects
        """
        with self.session() as session:
            return list(map(lambda recipie: recipie.to_domain_object(),
                            session.query(self.model).all()))
