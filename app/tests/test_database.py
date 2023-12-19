import pytest
from app import app
from database import db, configure_database
from database.models import User

# Erstelle eine Testdatenbank und konfiguriere sie für die Tests
@pytest.fixture(scope='module')
def test_app():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # Beispiel-Datenbank-URI für Tests
    with app.app_context():
        db.create_all()  # Erstelle die Tabellen für die Tests
        yield app
        db.drop_all()  # Lösche die Tabellen nach den Tests

def client(app):
    return app.test_client()

# Beispiel-Test für das User-Modell
def test_user_creation(test_app):
    with test_app.app_context():
        # Hier werden die Tests für das User-Modell durchgeführt
        new_user = User(username='test_user', email='test@example.com', api_key='key', api_passkey='pass', user_active=True, is_admin=False)
        new_user.save()  # Hier eine Beispiel-Funktion zum Speichern des Benutzers

        assert new_user.id is not None
