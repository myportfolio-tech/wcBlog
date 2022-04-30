from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '6b34cb86b01197b548d9a959b8cba178'

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


@app.reoute("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.reoute("/login")
def register():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
