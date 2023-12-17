from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #instância de aplicação web

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://EUFACOPROGRAMA:apXBE4kgASy6@ep-damp-waterfall-38037149.us-east-2.aws.neon.tech/mecanica_teste?sslmode=require'

database = SQLAlchemy(app) #fazendo a conexão com a instância

class Customer(database.Model):
    _tablename_ = 'customer'

    id_customer = database.Column(database.String, primary_key=True)
    number_customer = database.Column(database.Integer, nullable=False)
    address_customer = database.Column(database.String, nullable=False)
    name_customer = database.Column(database.String, nullable=False)
    car = database.Column(database.String, nullable=False)

class Item(database.Model):
    _tablename_ = 'item'

    id_item = database.Column(database.Integer, primary_key=True)
    name_item_request = database.Column(database.String, nullable=False)
    price = database.Column(database.Integer, nullable=False)

class Order_item(database.Model):
    _tablename_ = 'order_item'

    id_item = database.Column(database.Integer, primary_key=True)
    payment = database.Column(database.String, nullable=False)
    request = database.Column(database.String, nullable=False)
    service = database.Column(database.String, nullable=False)

class Employee(database.Model):
    _tablename_ = 'employee'

    id_employee = database.Column(database.String, primary_key = True)
    name_employee = database.Column(database.String, nullable = False)
    number_employee = database.Column(database.Integer, nullable = False)
    adress_employee = database.Column(database.String, nullable = False)
    wage_employee = database.Column(database.Float, nullable = False)
    date_born = database.Column(database.Date, nullable = False)

class Order(database.Model):
    _tablename_ = 'order_service'

    id_order = database.Column(database.Integer, primary_key=True)
    id_customer = database.Column(database.String, database.ForeignKey("customer.id_customer"), nullable=False)
    id_serv = database.Column(database.Integer, nullable=False)

class Payment(database.Model):
    _tablename_ = 'payment'

    id_pay = database.Column(database.Integer, primary_key=True)
    id_order = database.Column(database.Integer, database.ForeignKey("order_table.id_order"), nullable=False)
    name_pay = database.Column(database.String, nullable=False)
    portion = database.Column(database.Integer, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar_pedido', methods=['POST'])
def buscar_pedido():
    pedido_id = request.form['pedido_id']
    order_item = Order_item.query.get(pedido_id)

    if order_item:
        return render_template('sua_pagina.html', order_item=order_item)
    else:
        return render_template('sua_pagina.html', order_item=None)

@app.route('/pagina.html')
def pagina():
    return render_template('pagina.html')

@app.route('/cadastro.html')
def cadastro():
    return render_template('cadastro.html')

@app.route('/Login.html')
def Login():
    return render_template('Login.html')

@app.route('/service.html')
def service():
    return render_template('service.html')

if __name__ == '__main__':
    app.run(debug=True)