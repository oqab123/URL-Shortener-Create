import pytest 
from app import create_app  # Correct import statement

@pytest.fixture 
def app():
    app = create_app()
    yield app 

@pytest.fixture
def client(app):
    return app.test_client()
