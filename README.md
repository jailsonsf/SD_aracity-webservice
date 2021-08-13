<h1 align=center>Sistemas Distribuídos</h1>
<p align=center>Projeto para a disciplina de sistemas distribuídos sobre Web Services</p>

<h2 align=center>Aracity</h2>

## Descrição

Fechamento de compra\
O caixa da Aracity finaliza a compra armazenando a lista de produtos comprados no servidor. O servidor deve responder confirmando a compra ou não.

## O que foi usado?

* [Python 3](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Pony ORM](https://ponyorm.org/)

## Como executar?

Antes de rodar o projeto execute o comando:

```bash
pip3 install -r requirements.txt
```

1. Em um terminal aberto na raiz do projeto execute o comando:

```bash
python3 src/server/server.py
```

e em um novo terminal execute:

```bash
python3 src/client/client.py
```

2. No terminal onde o client está sendo executado, basta adicionar o input com dois números:

```bash
7 12
```

Onde o primeiro número é o código do produto e o segundo a quantidade desejada
E digitar 's' para adicionar mais produtos ou 'n' para finalizar a operação.

## Equipe

* [Jailson Soares](https://github.com/jailsonsf)
