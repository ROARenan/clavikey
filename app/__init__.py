from flask import Flask
from app.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from . import routes  # Importando as rotas
    app.register_blueprint(routes.bp)  # Registrando as rotas

    return app
