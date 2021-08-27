# App main view functions handling most common requests

from portal import db
from portal.main.models import User
from portal.main.forms import RegForm
from flask import redirect, url_for
from flask.templating import render_template
from . import main, auth



@main.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('main/index.html')


@auth.route('/registeration', methods = ['GET', 'POST'])
def register():
    form = RegForm()
    if form.validate_on_submit():
        user = User(reg_number = form.reg_number.data,
                    first_name = form.first_name.data,
                    last_name = form.last_name.data,
                    password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.index'))