import json
import requests
import time

from utils import clear

url_products = 'http://localhost:5000/products'
url_checkout = 'http://127.0.0.1:5000/checkout'


def get_all_products():
    response = requests.get(url_products)

    return response.json()


def add_order(products):
    response = requests.post(url_checkout, json=products)

    return response.json()


clear()
action = 1
while action != 0:
    time.sleep(1)

    print(
        'Opcoes:\n[0] Para sair\n[1] Listar todos os Produtos\n[2] Checkout')
    action = int(input())

    if action == 0:
        break

    elif action == 1:
        clear()
        products = get_all_products()
        print('Produtos disponíveis:')
        print('{:<6} {}'.format('ID', 'Produto'))
        print('--'*10)
        for produto in products['products']:
            print('{:<6} {}'.format(produto['id'], produto['nome']))
        print('--'*10)

    elif action == 2:
        print('Digite 0 para finalizar lista.')
        print('Digite o ID do produto e a quantidade que deseja.')
        order = {
            "products": []
        }
        while True:
            produto_id, amount = map(int, input().split())

            order['products'].append({'id': produto_id, 'amount': int(amount)})

            print('Adicionar mais um produto? N/s:')
            add_more = input().lower()

            if add_more == 'n':
                break

        resp = add_order(order)
        print(resp)
    else:
        print('Essa opção não existe!')
