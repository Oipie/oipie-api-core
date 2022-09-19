"""
    Configuration of dependency injection module
"""
from dependency_injector import containers, providers
from src.config.database import Database
from src.core.recipes.infrastructure.recipes_repository_sqlalchemy import (
    RecipesRepositorySQLAlchemy,
)
from src.core.users.infrastructure.user_repository_sqlalchemy import UsersRepositorySQLAlchemy
from src.core.users.application.users_registerer import UsersRegisterer
from src.shared.services.password.argon2_password import Argon2Password


class Container(containers.DeclarativeContainer):
    """
    Dependency injection container
    """

    wiring_config = containers.WiringConfiguration(packages=["..api", "src.api.auth"])

    db = providers.Singleton(Database)
    # pylint: disable=no-member
    recipes_repository = providers.Singleton(
        RecipesRepositorySQLAlchemy, session_factory=db.provided.session
    )
    users_repository = providers.Singleton(
        UsersRepositorySQLAlchemy, session_factory=db.provided.session
    )
    password_hasher = providers.Singleton(Argon2Password)
    users_registerer = providers.Singleton(
        UsersRegisterer, users_repository=users_repository, password_hasher=password_hasher
    )

    # pylint: enable=no-member
