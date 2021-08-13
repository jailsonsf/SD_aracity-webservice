from database.db import *
import json


@db_session
def all_products():
    result = select(p for p in Produto)[:]

    products = []
    for p in result:
        product = {
            "id": p.id,
            "nome": p.nome,
            "preco": p.preco,
            "quantidade": p.quantidade
        }

        products.append(product)

    response = json.dumps(products)

    return response


@db_session
def order(products):
    response = {
        'status': '',
        'total_price': 0
    }

    total_price = 0
    for p in products:
        result = select(c for c in Produto if c.id == p['id'])[:]
        product = result[0]
        print(product)

        if p['amount'] > product.quantidade:
            response['status'] = 'failed'
            response['msg'] = 'Compra cancelada! Itens adicionados excedem o estoque'

    items = []
    if response['status'] != 'failed':
        for p in products:

            result = select(c for c in Produto if c.id == p['id'])[:]
            product = result[0]

            items.append(product)

            total_price += product.preco * p['amount']

            product.quantidade -= p['amount']

        total_price = round(total_price, 2)
        response = {
            'status': 'approved',
            'total_price': total_price
        }

        sale = Pedido(
            status=response['status'],
            total_price=response['total_price'],
            items=items
        )

    commit()

    response = json.dumps(response)

    return response
