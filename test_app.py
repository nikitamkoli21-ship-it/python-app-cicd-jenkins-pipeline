import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_response_is_not_empty(client):
    response = client.get('/')
    assert response.data is not None

def test_basic_math():
    assert 2 + 2 == 4

def test_string_operations():
    assert "hello".upper() == "HELLO"

def test_list_operations():
    my_list = [1, 2, 3]
    assert len(my_list) == 3
    assert sum(my_list) == 6
