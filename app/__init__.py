from flask import Flask
from app.routes.SemanticServer import papers_bp  # Make sure this matches the actual file name

def create_app():
    app = Flask(__name__)
    app.register_blueprint(papers_bp, url_prefix='/api')
    return app
