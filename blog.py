from re import S
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy


# Config
app = Flask(__name__)
app.config['SECRET_KEY'] = '6b34cb86b01197b548d9a959b8cba178'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://site.db'
db = SQLAlchemy(app)


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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in successfully', 'success')
            return redirect(url_for('home'))
        else:
            flash('Loging failed. Please check email and password', 'danger')
    return render_template('login.html', title='Sign In', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
