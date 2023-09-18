from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Noelle Wavinya',
        'title': 'Blog post 1',
        'content': 'First Post Content',
        'date_posted': 'April 20, 2022'
    },
      {
        'author': 'Jane Doe',
        'title': 'Blog post 2',
        'content': 'Second Post Content',
        'date_posted': 'April 20, 2022'
    }
]

@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')


if __name__ == "__main__":
    app.run(debug = True)