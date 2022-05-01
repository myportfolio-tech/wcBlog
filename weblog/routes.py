from flask import render_template, url_for, flash, redirect, request
from weblog.forms import RegistrationForm, LoginForm
from weblog.models import User, Post
from weblog import app, db, bcrypt
from flask_login import login_user, logout_user, current_user, login_required

posts = [
    {
        'author': 'Eduardo',
        'title': 'Post 1',
        'content': 'First post content',
        'post_date': 'April, 29, 2022'
    },
    {
        'author': 'Eduardo 2',
        'title': 'Post 2',
        'content': 'Second post content',
        'post_date': 'April, 28, 2022'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pasword = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pasword)
        db.session.add(user)
        db.session.commit()
        flash(f'Your Account has Been Created. You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
        else:
            flash('Loging failed. Please check email and password', 'danger')
    return render_template('login.html', title='Sign In', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
