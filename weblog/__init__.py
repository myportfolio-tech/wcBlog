import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '6b34cb86b01197b548d9a959b8cba178'
# 'sqlite:///site.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://it:wecloudit@10.100.1.234:5432/weblog'
# os.environ.get('WE_BLOG_URI')
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('GOOGLE_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('GOOGLE_PASSWORD')

print(os.environ.get('GOOGLE_USER'))
print(os.environ.get('GOOGLE_PASSWORD'))

mail = Mail(app)

from weblog import routes