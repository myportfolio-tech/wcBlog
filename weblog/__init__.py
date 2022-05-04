import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '6b34cb86b01197b548d9a959b8cba178'
# 'sqlite:///site.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('WE_BLOG_URI')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://it:wecloudit@10.100.1.234:5432/weblog'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from weblog import routes