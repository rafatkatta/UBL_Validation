from flask import Flask
from database import configure_database

# Erstelle die Flask-Anwendung
app = Flask(__name__)

# Konfiguriere die Datenbank für diese Anwendung
configure_database(app)

# Restlicher Code für dein Modul ...
