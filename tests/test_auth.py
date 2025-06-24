def test_successful_auth(client, token):
    token = client.auth("admin", "password123")
    assert isinstance(token, str) and len(token) > 0
