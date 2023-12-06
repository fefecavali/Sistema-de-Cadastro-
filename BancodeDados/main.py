from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from classes import Customer, Item, Item_pedido, Employee, Order, Payment  # Importando as entidades do arquivo models.py

# Criar engine e sessão
engine = create_engine('postgresql://postgres:pgadmin123@localhost:5432/mecanica_teste')
Session = sessionmaker(bind=engine)
session = Session()


# read
clientes = session.query(Customer).all()
for cliente in clientes:
    print(cliente)

# Fechar a sessão
session.close()

# '----> INSERT <----'

insertF = Customer(id_customer="21499845678", number_customer=998058909, address_customer="Rua Mambore bonita", name_customer="Fernanda", car="Ferrari 2025")
insertS = Item(id_item=22, name_item_request="Vela", price=20)
insertB= Item_pedido(id_item=22, payment="dinheiro", request="a vista", service="vela queimada")
insertP = Order ( id_order=12345678910, id_customer="21499845678" ,id_serv=12343534)
insertP = Payment (id_pay=123456, id_order=12345678910, name_pay="pix", portion=12)

# inserindo

session.add(insertF)
session.add(insertS)
session.add(insertB)
session.add(insertP)
session.add(insertP)

session.commit()

queryFe = session.query(Customer).all()
queryS = session.query(Item).all()
queyB = session.query(Item_pedido).all()
queryP = session.query(Order).all()
queryP2 = session.query(Payment).all()

session.commit()

'----> UPDATE <----'
session.query(Customer).filter(Customer.id_customer == "21499845678").update( { "name_customer" : "Fernanda Cavali"})
session.query(Item).filter(Item.id_item == 22).update( { "name_item_pedido" : "Cabo de vela"})
session.query(Item_pedido).filter(Item_pedido.id_item == 22).update( { "service" : "vela ruim"})
session.query(Order).filter(Order.id_order == 12345678910).update( { "id_customer" : "87332199021"})
session.query(Payment).filter(Payment.id_pay == 123456).update( { "name_pay" : "cartão"})

session.commit()

# # '----> DELETE <----'

# # session.query(Customer).filter(Customer.id_customer == "21499845678").delete()
# # session.query(Item).filter(Item.id_item == 22).delete()
# # session.query(Item_pedido).filter(Item_pedido.id_item == 22).delete()


# Fechar conexão
session.close()  
