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
    assert b"Agile Sprint Board" in response.data

def test_get_tickets(client):
    response = client.get('/api/tickets')
    assert response.status_code == 200
    tickets = response.get_json()
    assert len(tickets) >= 3

def test_create_and_move_ticket(client):
    # 1. Create a ticket
    post_res = client.post('/api/tickets', json={"title": "Test CI Pipeline", "priority": "High"})
    assert post_res.status_code == 201
    ticket_id = post_res.get_json()["id"]

    # 2. Move ticket to in_progress
    move_res = client.post(f'/api/tickets/{ticket_id}/move', json={"status": "in_progress"})
    assert move_res.status_code == 200
    assert move_res.get_json()["status"] == "in_progress"

def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json()["status"] == "up"