"""
This module serves the purpose of perform several actions on the recipes
"""

from dependency_injector.wiring import Provide, inject
from flask import Blueprint, request
from src.config.container import Container
from src.api.shared.dtos.paginated_response_dto import PaginatedResponseDTO
from src.core.recipes.application.recipes_lister import RecipesLister
from src.core.recipes.infrastructure.recipes_repository_sqlalchemy import (
    RecipesRepositorySQLAlchemy,
)


recipes_bp = Blueprint("recipes_bp", __name__)


@recipes_bp.route("/recipes", methods=["GET"])
@inject
def index(recipes_repository: RecipesRepositorySQLAlchemy = Provide[Container.recipes_repository]):
    """
    This route returns a 200 OK returning all recipes existing in database
    """

    offset = request.args.get("offset", default=0, type=int)
    limit = request.args.get("limit", default=10, type=int)

    lister = RecipesLister(recipes_repository)

    recipies, total_recipies = lister.execute(offset, limit)
    return PaginatedResponseDTO.serialize(
        list(map(lambda recipie: recipie.serialize(), recipies)), total_recipies
    )
