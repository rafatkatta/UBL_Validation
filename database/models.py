from . import db  # Hier wird 'db' aus der Datenbankkonfiguration importiert

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    api_key = db.Column(db.String(50), nullable=False)
    api_passkey = db.Column(db.String(50), nullable=False)
    user_active = db.Column(db.Boolean, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default= False)
    def save(self):
      db.session.add(self)
      db.session.commit()