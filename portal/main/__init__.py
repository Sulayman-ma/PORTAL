# Main application sub-package
from flask import Blueprint


# app main and authentication blueprints
main = Blueprint('main', __name__)

# import views into blueprint after creating it
# importing before creating blueprint would give import issues
# something about a circular import
from . import views