# Application factory

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import configs
from .main import main


db = SQLAlchemy()


def create_app(config_name):
    """Creates the application instance according to configuration passed as argument. Initializes the app extensions, registers blueprints.

    Return: application instance
    """
    app = Flask(__name__)

    # TODO: Importing app configuratins
    app.config.from_object(configs[config_name])
    configs[config_name].init_app(app)

    # TODO: Initializing extensions
    db.init_app(app)
    
    # TODO: Blueprint registeration
    app.register_blueprint(main)

    # Final application instance
    return app