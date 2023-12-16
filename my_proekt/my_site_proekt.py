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
@app.route('/ph1', methods=['POST','GET'])
def create_article_ph1():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        create_index(title, price)
        return redirect('/ph1')
    else:
        return render_template('phone1.html')
@app.route('/ph2', methods=['POST','GET'])
def create_article_ph2():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        create_index(title, price)
        return redirect('/ph2')
    else:
        return render_template('phone2.html')
@app.route('/ph3', methods=['POST','GET'])
def create_article_ph3():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        create_index(title, price)
        return redirect('/ph3')
    else:
        return render_template('phone3.html')
@app.route('/ph4', methods=['POST','GET'])
def create_article_ph4():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        create_index(title, price)
        return redirect('/ph4')
    else:
        return render_template('phone4.html')
@app.route('/ph5', methods=['POST','GET'])
def create_article_ph5():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        create_index(title, price)
        return redirect('/ph5')
    else:
        return render_template('phone5.html')
@app.route('/ph6', methods=['POST','GET'])
def create_article_ph6():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        create_index(title, price)
        return redirect('/ph6')
    else:
        return render_template('phone6.html')
@app.route('/aud1', methods=['POST','GET'])
def create_article_aud1():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        create_index(title, price)
        return redirect('/aud1')
    else:
        return render_template('audio1.html')
@app.route('/aud2', methods=['POST','GET'])
def create_article_aud2():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        create_index(title, price)
        return redirect('/aud2')
    else:
        return render_template('audio2.html')
@app.route('/aud3', methods=['POST','GET'])
def create_article_aud3():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        create_index(title, price)
        return redirect('/aud3')
    else:
        return render_template('audio3.html')
@app.route('/aud4', methods=['POST','GET'])
def create_article_aud4():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        create_index(title, price)
        return redirect('/aud4')
    else:
        return render_template('audio4.html')
@app.route('/aud5', methods=['POST','GET'])
def create_article_aud5():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        create_index(title, price)
        return redirect('/aud5')
    else:
        return render_template('audio5.html')
@app.route('/aud6', methods=['POST','GET'])
def create_article_aud6():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        create_index(title, price)
        return redirect('/aud6')
    else:
        return render_template('audio6.html')
app.run(debug=True)