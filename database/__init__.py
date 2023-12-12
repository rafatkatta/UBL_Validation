from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure_database(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

# Importiere deine Modelle hier, um die Datenbank zu erstellen
from . import models
