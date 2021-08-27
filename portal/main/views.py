# App main view functions handling most common requests

from flask.templating import render_template
from . import main


@main.route('/', methods = ['GET'])
def index():
    return render_template('main/index.html')
