from flask import Flask, render_template, url_for, request, redirect

from DB import create_index, show_table, select_index, delete_index, update_index,create_table,price_d

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('okel.html')
@app.route('/aud')
def aud():
    return render_template('okelaudio.html')
@app.route('/ph')
def ph():
    return render_template('okelphones.html')


@app.route('/busk/')
def busk():
    price = price_d()
    articles = show_table()
    return render_template('busk.html', articles=articles,price = price)


@app.route('/busk/delete(<int:id>)')
def post_delete(id):
    delete_index(id)
    return redirect('/busk')


# @app.route('/posts/<int:id>/update', methods=['POST', 'GET'])
# def post_update(id):
#     article = select_index(id)[0]
#     if request.method == 'POST':
        
#         update_index(title,price)
#         return redirect('/posts/')
#     return render_template('post-update.html', article=article)


@app.route('/pc1', methods=['POST','GET'])
def create_article_pc1():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        create_index(title, price)
        return redirect('/pc1')
    else:
        return render_template('pc1.html')
@app.route('/pc2', methods=['POST','GET'])
def create_article_pc2():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        create_index(title, price)
        return redirect('/pc2')
    else:
        return render_template('pc2.html')
@app.route('/pc3', methods=['POST','GET'])
def create_article_pc3():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        create_index(title, price)
        return redirect('/pc3')
    else:
        return render_template('pc3.html')
@app.route('/pc4', methods=['POST','GET'])
def create_article_pc4():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        create_index(title, price)
        return redirect('/pc4')
    else:
        return render_template('pc4.html')
@app.route('/pc5', methods=['POST','GET'])
def create_article_pc5():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        create_index(title, price)
        return redirect('/pc5')
    else:
        return render_template('pc5.html')
@app.route('/pc6', methods=['POST','GET'])
def create_article_pc6():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        create_index(title, price)
        return redirect('/pc6')
    else:
        return render_template('pc6.html')


app.run(debug=True)