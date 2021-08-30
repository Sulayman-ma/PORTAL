# App's view functions handling most common requests

from portal import db
from portal.models import User
from portal.main.forms import RegForm
from flask import redirect, url_for
from flask.templating import render_template
from . import main



@main.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('main/index.html')
