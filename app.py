import sqlalchemy as sa
import sqlalchemy.orm as so
from app.models import User
from app import app, db

@app.shell_context_processor
def make_shell_context():
    return {'so': so, 'sa': sa, 'db': db, 'User': User}