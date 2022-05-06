import os
import secrets
from PIL import Image
from flask import url_for
from flask_mail import Message
from weblog import app, mail


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profiles', picture_fn)
    
    # Resize Picture
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

   # Save new picture 
    i.save(picture_path)
    
    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Rester Request', 
                    sender='eduardo@myportfolio.tech', 
                    recipients=[user.email, 'eduardo@doahfest.com'])
    msg.body = f""" To Reset your password, follow this link:
{url_for('users.reset_password', token=token, _external=True)}
If you did not make this request, please ignore this message.
    """
    mail.send(msg)