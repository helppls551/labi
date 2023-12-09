from flask import Flask, render_template, url_for,request,redirect

import myDB
app = Flask(__name__)
app.config['SOLACHEMY_DATABASE_URI'] = 'sqlite:///blog.db'


@app.route('/')
def index():
    names = []
    return render_template('base.html',lst = names)

@app.route('/statue',methods =["POST","GET"])
def statue():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']
        myDB.create_index(title=title,intro=intro,text = text)
        return redirect('/')
    else:
        return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')


app.run(debug=True)
