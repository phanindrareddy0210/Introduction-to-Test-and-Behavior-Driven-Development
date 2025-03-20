from flask import Flask, jsonify, request

app = Flask(__name__)

products = []

@app.route('/products', methods=['GET'])
def list_all():
    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def read(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    return jsonify(product) if product else ('', 404)

@app.route('/products', methods=['POST'])
def create():
    new_product = request.json
    new_product["id"] = len(products) + 1
    products.append(new_product)
    return jsonify(new_product), 201

@app.route('/products/<int:product_id>', methods=['PUT'])
def update(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return ('', 404)
    product.update(request.json)
    return jsonify(product)

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete(product_id):
    global products
    products = [p for p in products if p["id"] != product_id]
    return ('', 204)

@app.route('/products/search', methods=['GET'])
def search():
    name = request.args.get('name')
    category = request.args.get('category')
    available = request.args.get('available')

    results = products
    if name:
        results = [p for p in results if name.lower() in p['name'].lower()]
    if category:
        results = [p for p in results if category.lower() == p['category'].lower()]
    if available:
        available = available.lower() == 'true'
        results = [p for p in results if p['available'] == available]

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)

