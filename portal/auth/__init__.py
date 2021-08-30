# Application authentication sub-package
from flask import Blueprint

# authentication blueprint
auth = Blueprint('auth', __name__)


from . import views