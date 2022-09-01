"""
Tests recipes lister
"""
from src.core.recipes.domain.recipe import Recipe
from src.core.recipes.infrastructure.recipes_repository_fake import RecipesRepositoryFake
from src.tests.fixtures.recipe_fixture import PANCAKE, STRAWBERRY_SMOOTHIE
from .recipes_lister import RecipesLister


def test_serialize_is_ok():
    """
    Checks that all elements are returned
    """
    recipes = [Recipe(PANCAKE), Recipe(STRAWBERRY_SMOOTHIE)]
    recipe_repository = RecipesRepositoryFake(recipes)
    recipe_lister = RecipesLister(recipe_repository)

    result = recipe_lister.execute()

    assert len(result) == 2
    assert result[0].name == PANCAKE.get('name')
    assert result[1].name == STRAWBERRY_SMOOTHIE.get('name')
