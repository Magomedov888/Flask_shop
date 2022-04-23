from shop import app
from flask import render_template
from shop.models import Product

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/single_blog')
def single_blog():
    return render_template('single_blog.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/single_product')
def single_product():
    return render_template('single_product.html')

@app.route('/category')
def category():
    return render_template('category.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/tracking_order')
def tracking_order():
    return render_template('tracking_order.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')