"""
    Configuration of dependency injection module
"""
from dependency_injector import containers, providers
from src.config.database import Database
from src.config.jwt import JWT_SECRET_KEY
from src.core.recipes.infrastructure.recipes_repository_sqlalchemy import (
    RecipesRepositorySQLAlchemy,
)
from src.core.users.infrastructure.user_repository_sqlalchemy import UsersRepositorySQLAlchemy
from src.core.users.application.users_registerer import UsersRegisterer
from src.core.users.application.users_login import UsersLogin
from src.shared.services.password.argon2_password import Argon2Password
from src.shared.services.tokenizer.jwt_tokenizer import JwtTokenizer


class Container(containers.DeclarativeContainer):
    """
    Dependency injection container
    """

    wiring_config = containers.WiringConfiguration(packages=["..api", "src.api.auth"])

    db = providers.Singleton(Database)
    tokenizer = JwtTokenizer(JWT_SECRET_KEY)

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
    users_login = providers.Singleton(
        UsersLogin,
        users_repository=users_repository,
        password_hasher=password_hasher,
        tokenizer=tokenizer,
    )

    # pylint: enable=no-member
