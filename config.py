from os.path import dirname, abspath, join
from os import environ, stat



base_dir = abspath(dirname(__file__))

# per configuration, we use classes
class Config:
    # Base config class with settings shared by all configurations
    SECRET_KEY = '<secret key here>'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        # function implemented by extensions in their own way
        pass


class Development(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(base_dir, 'dev.sqlite')


class Testing(Config):
    pass

# config dict to be exported as needed 
configs = {
    'dev': Development,
    'test': Testing,
    
    'default': Development
}