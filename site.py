from flask import Flask,render_template,url_for
import os
folder = os.getcwd
app = Flask(__name__,template_folder= 'F:\GR\templates' ,static_folder= '')


@app.route('/')
def index():
    names = []
    return render_template('base.html',lst = names)


@app.route('/about')
def about():
    return render_template('about.html')


app.run(debug=True)
