"""
Tests to check health SHOW endpoint
"""


def test_show_health(client):
    """
    This test checks if API is up
    """
    response = client.get("/health")
    assert response.status_code == 204
