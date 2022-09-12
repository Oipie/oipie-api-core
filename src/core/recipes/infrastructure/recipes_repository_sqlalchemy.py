"""
SQLAlchemy repository for Recipes
"""
from typing import Callable
from contextlib import AbstractContextManager
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

    def find_all(self, offset: int, limit: int) -> tuple[list[Recipe], int]:
        """
        Gets all recipes from database and returns domain objects
        """
        with self.session() as session:
            query = session.query(RecipeModel)
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
