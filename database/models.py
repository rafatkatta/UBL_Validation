from . import db  # Hier wird 'db' aus der Datenbankkonfiguration importiert

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    api_key = db.Column(db.String(50), nullable=False)
    api_passkey = db.Column(db.String(50), nullable=False)
