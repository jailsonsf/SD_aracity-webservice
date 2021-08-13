import json
from flask import Flask, jsonify, request, abort

from database.db import *
from controller import *

with db_session:
    if Produto.select().first() is None:
        populate_database()

app = Flask(__name__)


@app.route('/products', methods=['GET'])
def list_products():
    resp = jsonify({'products': json.loads(all_products())})

    return resp


@app.route('/checkout', methods=['POST'])
def checkout():
    if not request.json or not 'products' in request.json:
        abort(400)

    sale = order(request.json['products'])

    resp = jsonify(json.loads(sale))

    return resp, 201


if __name__ == '__main__':
    print('Servidor no ar!')
    app.run(host='0.0.0.0', debug=True)
