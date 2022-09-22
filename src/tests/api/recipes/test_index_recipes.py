"""
Tests to check recipes INDEX endpoint
"""


def test_index_recipes_works(api_client):
    """
    This test checks if /recipes endpoint is up
    """

    response = api_client.get_recipes()

    assert response["items"] == []
    assert response["meta"]["totalItems"] == 0
