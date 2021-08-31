from flask_migrate import Migrate
from portal import db, create_app
from portal.models import User


app = create_app('dev')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db = db, User = User)


app.run(debug = True)
