from flask import Flask
from flask_cors import CORS
from app.routes.SemanticServer import semantic_bp
from app.routes.CrossRefServer import crossRef_bp
def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(semantic_bp, url_prefix='/api')
    app.register_blueprint(crossRef_bp, url_prefix='/api')
    return app
    