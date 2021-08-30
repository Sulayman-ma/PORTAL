from portal import db
from portal.models import User
from portal.main.forms import RegForm
from flask import redirect, url_for
from flask.templating import render_template
from . import auth



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
    return render_template('auth/register.html', form = form)