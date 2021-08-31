# from flask_login import current_user
from os import abort
from os.path import splitext
from flask import redirect, url_for, render_template, request
from wtforms.validators import ValidationError
from . import auth
from .forms import RegForm
from .. import db, photos
from ..models import User



@auth.route('/registeration', methods = ['GET', 'POST'])
def register():
    form = RegForm()
    if form.validate_on_submit() and 'photo' in request.files:
        user = User(reg_number = form.reg_number.data,
                    first_name = form.first_name.data,
                    last_name = form.last_name.data,
                    department = form.department.data,
                    level = form.level.data,
                    password = form.password.data)

        # rename file using student reg_number
        _, file_ext = splitext(request.files['photo'].filename)
        new_name = '{}{}'.format(user.reg_number, file_ext)
        photos.save(request.files['photo'], name = new_name)

        # add user and commit
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', form = form)