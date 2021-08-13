from pony.orm import *

db = Database('sqlite', './database.db', create_db=True)


class Produto(db.Entity):
    nome = Required(str)
    preco = Required(float)
    quantidade = Required(int)
    pedidos = Set('Pedido')


class Pedido(db.Entity):
    id = PrimaryKey(int, auto=True)
    status = Required(str)
    total_price = Required(float)
    items = Set(Produto)


# sql_debug(True)


db.generate_mapping(create_tables=True)


@db_session
def populate_database():
    produto1 = Produto(nome='Tinta', preco=10.85, quantidade=10)
    produto2 = Produto(nome='Tubos', preco=13.00, quantidade=15)
    produto3 = Produto(nome='Interruptor', preco=9.50, quantidade=17)
    produto4 = Produto(nome='Cabos', preco=15.00, quantidade=18)
    produto5 = Produto(nome='Furadeira', preco=29.90, quantidade=5)
    produto6 = Produto(nome='Lâmpadas', preco=16.90, quantidade=18)
    produto7 = Produto(nome='Pregos', preco=5.45, quantidade=40)
    produto8 = Produto(nome='Alicate', preco=14.00, quantidade=8)
    produto9 = Produto(nome='Martelo', preco=13.75, quantidade=9)
    produto10 = Produto(nome='Madeira', preco=19.00, quantidade=12)

    commit()
