# Parte das consultas

from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from classes import Customer, Item, Order_item, Employee, Order, Payment

engine = create_engine('postgresql://EUFACOPROGRAMA:apXBE4kgASy6@ep-damp-waterfall-38037149.us-east-2.aws.neon.tech/mecanica_teste?sslmode=require')
Session = sessionmaker(bind=engine)
session = Session()

'--> consultas Bruno'

'--> consultas Fernanda'
#1 Retorne o cliente que possui o id 7890123456
id="7890123456"
cliente1 = session.query(Customer).filter_by(id_customer=id).first()

if cliente1:
    print(cliente1)
else:
    print(f'Cliente {id} não encontrado.')

#2 Retorne os carros dos clientes moram na "Avenida araruna fedida"

address = "Avenida araruna fedida"
carros_cliente2 = session.query(Customer).filter_by(address_customer=address).all()
for i in carros_cliente2:
    print(f"Cliente: {i.name_customer} possui o carro: {i.car}")

#3

'--> consultas Lara'

'--> consultas Pedro'

#1
all = session.query(Order).all()
print(all)
session.commit()
#2
orders_ordered = session.query(Order).order_by(Order.id_order).all()
print(orders_ordered)
session.commit()
#3
specific_orders = session.query(Order).filter(Order.id_customer == '21499845678').all()
print(specific_orders)
session.commit()

'--> consultas Sara'

#1
data = session.query(Employee).all() #selecionando tudo da tabela employee
print(data[2].wage_employee,data[4].wage_employee) #pegando o salario do objeto na posição 02
session.commit()
#2
data2 = session.query(Employee).filter(Employee.name_employee == 'Sara Guaiume').all()
print(data2)
#3
data3 = session.query(Employee).filter(Employee.wage_employee < 2000).order_by(Employee.number_employee).all()
print(data3)
