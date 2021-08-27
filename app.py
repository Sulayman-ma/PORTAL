from portal import db, create_app
from portal.main.models import User


app = create_app('dev')


@app.shell_context_processor
def make_shell_context():
    return dict(db = db, User = User)