from urlshort import create_app

def test_shorten(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Shorten' in response.data