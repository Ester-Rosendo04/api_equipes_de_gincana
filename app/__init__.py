import os

from flask import Flask
from .routes.participants import participants_bp
from .routes.teams import teams_bp
from .routes.auth import auth_bp
from .routes.users import users_bp
from .config import Config
from .extensions import db, migrate, ma, jwt
from marshmallow import ValidationError
from werkzeug.exceptions import NotFound

def create_app():
    app = Flask(__name__)

    app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY", "fallback_inseguro")

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    jwt.init_app(app)

    from app.models import participant, team

    app.register_blueprint(participants_bp, url_prefix="/participants")
    app.register_blueprint(teams_bp, url_prefix="/teams")
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(users_bp, url_prefix="/users")

    @app.errorhandler(ValidationError)
    def handle_validation_error(err):
        return {"success": False, "errors": err.messages}, 400

    @app.errorhandler(NotFound)
    def handle_not_found(err):
        return {
            "success": False,
            "errors": "Recurso não encontrado"
        }, 404

    @app.errorhandler(404)
    def handle_404_error(err):
        return {
            "success": False,
            "message": "Recurso não encontrado"
        }, 404

    return app