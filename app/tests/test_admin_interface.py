import json
import pytest
from app import app

@pytest.fixture

def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_user(client):
    # Beispiel-Daten für den zu erstellenden Benutzer
    user_data = {
        'username': 'testuser',
        'email': 'testuser@example.com'
    }
    # Senden der POST-Anfrage zum Erstellen des Benutzers
    response = client.post('/admin/create/user', json=user_data)
    
    # Überprüfen, ob die Anfrage erfolgreich war (Statuscode 201)
    assert response.status_code == 201

    # Überprüfen, ob die Antwort die erwarteten Daten enthält
    data = json.loads(response.data)
    assert 'api_key' in data
    assert 'api_passkey' in data
    assert data['email'] == 'testuser@example.com'

def test_get_user_exists(client):
    # Test für existierenden Benutzer
    response = client.get('/api/user?username=user1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == 'Benutzer existiert.'

def test_get_user_not_exists(client):
    # Test für nicht existierenden Benutzer
    response = client.get('/api/user?username=nonexistent_user')
    assert response.status_code == 404
    
    content = response.data.decode('utf-8')
    # Überprüfe, ob der Inhalt der Antwort das erwartete Muster enthält
    assert 'Benutzer existiert nicht.' in content

def test_update_user(client):
    # Test für das Aktualisieren eines Benutzers
    response = client.put('/api/user/update?username=user1', json={"new_username": "new_user1"})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == 'Benutzer erfolgreich aktualisiert.'

def test_create_new_user(client):
    # Test für das Erstellen eines Benutzers
    new_user_data = {'username': 'new_user1', 'email': 'new_user1@example.com'}
    response = client.post('/admin/create/user', json=new_user_data)
    assert response.status_code == 201
    data = json.loads(response.data)
    assert 'api_key' in data  # Überprüfe, ob die Antwort die erwarteten Daten enthält
    assert 'api_passkey' in data

def test_delete_user(client):
    test_create_new_user(client)
    # Test für das Löschen eines Benutzers
    response = client.delete('/api/user/delete?username=new_user1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == 'Benutzer erfolgreich gelöscht.'
