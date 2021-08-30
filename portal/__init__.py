# Application factory

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import configs



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
    # blueprint cannot be imported at top
    # this is that circular import I mentioned back there
    from .main import main
    from .auth import auth

    app.register_blueprint(main)
    app.register_blueprint(auth)

    # Final application instance
    return app