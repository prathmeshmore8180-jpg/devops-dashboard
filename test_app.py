import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_dashboard_status_code(client):
    response = client.get('/')
    assert response.status_code == 200

def test_dashboard_content(client):
    response = client.get('/')
    assert b"DevOps Service Monitor" in response.data
    assert b"System Status" in response.data

def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["status"] == "up"
    assert "timestamp" in json_data
