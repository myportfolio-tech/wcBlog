from weblog import db
from weblog.models import User, Post

db.drop_all()
db.create_all()
db.session.commit()