# Parte das consultas

from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from classes import Customer, Item, Order_item, Employee, Order, Payment

engine = create_engine('postgresql://EUFACOPROGRAMA:apXBE4kgASy6@ep-damp-waterfall-38037149.us-east-2.aws.neon.tech/mecanica_teste?sslmode=require')
Session = sessionmaker(bind=engine)
session = Session()

'--> consultas Bruno'

'--> consultas Fernanda'

'--> consultas Lara'

'--> consultas Pedro'

#1
all = session.query(Order).all()
#2
orders_ordered = session.query(Order).order_by(Order.id_order).all()
#3
specific_orders = session.query(Order).filter(Order.id_customer == '21499845678').all()

'--> consultas Sara'