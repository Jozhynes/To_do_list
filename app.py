from flask import Flask, render_template
from sqlalchemy.orm import sessionmaker
app=Flask(__name__)


@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__=='__main__':
    app.run(debug=True)