from flask import Flask, render_template

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
