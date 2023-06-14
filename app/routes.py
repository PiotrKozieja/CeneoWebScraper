from app import app
from flask import Flask, render_template, request, redirect, url_for

@app.route("/")
def index():
    return render_template('main_page.html')

@app.route("/name",defaults={'name' :"Anonim"})
@app.route("/name/<name>")
def name(name):
    return f"Hello {name}"

@app.route("/o_autorze")
def author():
    return render_template('about_author.html')

@app.route("/ekstrakcja", methods=['POST','GET'])
def extraction():
    if request.method == 'POST':
        product_code = request.form.get('product_code')
        return redirect(url_for('product', code=product_code))
    return render_template('extraction.html')

@app.route("/lista_produktow")
def productList():
    return render_template('product_list.html')

@app.route("/product/<code>")
def product(code):
    return render_template('product.html', product_code=code)

@app.route("/wykresy")
def charts():
    return render_template('charts.html')