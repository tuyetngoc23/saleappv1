import json

def read_data(path  ='data/product.json'):
    with open(path, encoding='utf-8') as f:
        return json.load(f)

def get_product_id(product_id):
    product = read_data('data/product.json')
    for p in product:
        if p["id"] == product_id:
            return p