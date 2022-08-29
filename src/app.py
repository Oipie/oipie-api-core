"""
Main entrypoint
"""
from flask import Flask
from .api.health.healthcontroller import health_bp

app = Flask(__name__)

app.register_blueprint(health_bp)

if __name__ == "__main__":
    app.run()
