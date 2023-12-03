from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    names = []
    return render_template('index.html',lst = names)


@app.route('/about')
def about():
    return render_template('about.html')


app.run(debug=True)
