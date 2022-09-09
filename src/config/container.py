"""
    Configuration of dependency injection module
"""
from dependency_injector import containers, providers
from src.config.database import Database
from src.core.recipes.infrastructure.recipes_repository_sqlalchemy import (
    RecipesRepositorySQLAlchemy,
)


class Container(containers.DeclarativeContainer):
    """
    Dependency injection container
    """

    wiring_config = containers.WiringConfiguration(packages=["..api"])

    db = providers.Singleton(Database)
    # pylint: disable=no-member
    recipes_repository = providers.Factory(
        RecipesRepositorySQLAlchemy, session_factory=db.provided.session
    )

    # pylint: enable=no-member
