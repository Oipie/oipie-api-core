"""
Tests to check recipes INDEX endpoint
"""


def test_index_recipes_works(client):
    """
    This test checks if /recipes endpoint is up
    """
    response = client.get("/recipes")

    assert response.status_code == 200
    assert response.json["items"] == []
    assert response.json["meta"]["totalItems"] == 0
