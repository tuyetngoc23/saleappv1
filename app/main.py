from flask import render_template
from app import app, utils

@app.route("/")
def index():
    categories = utils.read_data('data/categories.json')
    return render_template('index.html', categories = categories)

@app.route("/product")
def product_list():
    product = utils.read_data('data/product.json')
    return render_template('product.html', product=product)

"""@app.route("/product/<int:product_id>")
def product_detail(product_id):
    product = utils.get_product_id(product_id = product_id)
    return render_template('product_detail.html', product = product)"""


if __name__ == "__main__":
    app.run(debug=True)
