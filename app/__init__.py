from flask import Flask
from app.admin.admin_interface import admin_interface_bp

app = Flask(__name__)
app.register_blueprint(admin_interface_bp)

if __name__ == "__main__":
    app.run(debug=True)
