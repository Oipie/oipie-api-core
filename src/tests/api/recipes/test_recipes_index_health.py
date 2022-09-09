"""
Tests to check recipes INDEX endpoint
"""


from src.core.recipes.domain.recipe import Recipe
from src.core.recipes.infrastructure.recipes_repository_fake import RecipesRepositoryFake
from src.tests.fixtures.recipe_fixture import PANCAKE, STRAWBERRY_SMOOTHIE


def test_recipes_index_health(client, app):
    """
    This tests ensure recipe listing.
    """
    pancake = Recipe(PANCAKE)
    strawberry_smoothie = Recipe(STRAWBERRY_SMOOTHIE)
    recipes_repository = RecipesRepositoryFake([pancake, strawberry_smoothie])

    app.container.recipes_repository.override(recipes_repository)
    response = client.get("/recipes")
    data = response.json
    length = len(data)
    assert response.status_code == 200
    assert length == 2
