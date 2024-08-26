import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_shorten(client):
    response = client.get('/')
    assert b'Shorten' in response.data
