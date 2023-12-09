from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from classes import Customer, Item, Order_item, Employee, Order, Payment
from datetime import date
 
# Importando as entidades do arquivo classes.py

# Criar engine e sessão
engine = create_engine('postgresql://EUFACOPROGRAMA:apXBE4kgASy6@ep-damp-waterfall-38037149.us-east-2.aws.neon.tech/mecanica_teste?sslmode=require')
Session = sessionmaker(bind=engine)
session = Session()


# '----> INSERT <----'   obs: Professor nesa parte usamos o chat para termos criatividade de criarmos tantos objetos das classes, esperamos que não tenha problema

insert_customer = [Customer(
        id_customer="21499845678",
        number_customer=998058909,
        address_customer="Rua Mambore bonita",
        name_customer="Fernanda",
        car="Ferrari 2025"),
    Customer(
        id_customer="052013024", 
        number_customer=876543210, 
        address_customer="Rua campo mourinho", 
        name_customer="Lara Deitos", 
        car="Toyota Corolla"),
    Customer(
        id_customer="4567891230",
        number_customer=987654321,
        address_customer="Rua campo mourao",
        name_customer="Sara Guaiume",
        car="Tesla 2024"),
    Customer(
        id_customer="7890123456",
        number_customer=14235465,
        address_customer="Avenida araruna fedida",
        name_customer="Pedro Utumi",
        car="Mercedes 2023"),
    Customer(
        id_customer="1234567890",
        number_customer=10987642,
        address_customer="Rua dos de Beltao",
        name_customer="Bruno Pena",
        car="Audi 2022"),
    Customer(
        id_customer="987654321",
        number_customer=234534,
        address_customer="Rua das Acácias",
        name_customer="Professor Eduardo",
        car="BMW 2021")
]
insert_itens = [ Item(id_item=22, name_item_request="Vela", price=20), 
    Item(id_item=40, name_item_request="Óleo do Motor", price=30),
    Item(id_item=41, name_item_request="Filtro de Óleo", price=15),
    Item(id_item=42, name_item_request="Pastilhas de Freio", price=50),
    Item(id_item=43, name_item_request="Filtro de Ar", price=20),
    Item(id_item=44, name_item_request="Bateria", price=80) ]

insert_orderItens =  [
    Order_item(id_item=22, payment="dinheiro", request="a vista", service="vela queimada"),  
    Order_item(id_item=40, payment="cartão", request="parcelado", service="troca de óleo"),
    Order_item(id_item=41, payment="cartão", request="à vista", service="troca de filtro de óleo"),
    Order_item(id_item=42, payment="dinheiro", request="parcelado", service="substituição das pastilhas de freio"),
    Order_item(id_item=43, payment="dinheiro", request="parcelado", service="troca de filtro de ar"),
    Order_item(id_item=44, payment="cartão", request="parcelado", service="substituição da bateria")]

insertEmployee = [
    Employee(id_employee='123456789',name_employee='John Doe',number_employee=123, adress_employee='123 Main Street',wage_employee=2500.00, date_born=date(1990, 5, 15)),
    Employee(id_employee='234567890', name_employee='Alice', number_employee=123456789, adress_employee='Rua A', wage_employee=3000.0, date_born='1990-05-15'),
    Employee(id_employee='345678901', name_employee='Bob', number_employee=234567890, adress_employee='Rua B', wage_employee=3500.0, date_born='1985-08-22'),
    Employee(id_employee='456789012', name_employee='Carol', number_employee=345678901, adress_employee='Rua C', wage_employee=3200.0, date_born='1993-12-10'),
    Employee(id_employee='567890123', name_employee='David', number_employee=456789012, adress_employee='Rua D', wage_employee=3100.0, date_born='1988-04-30'),
    Employee(
    id_employee='678901234',
    name_employee='Sophia',
    number_employee=567890123,
    adress_employee='Rua E',
    wage_employee=3200.0,
    date_born='1995-10-15')  ]

insertOrder = [ 
    Order( id_order=123456789, id_customer="21499845678" ,id_serv=12343534),
    Order(id_order=123456790, id_customer="7890123456", id_serv=98765432),
    Order(id_order=123456791, id_customer="4567891230", id_serv=45678912),
    Order(id_order=123456792, id_customer="052013024", id_serv=56789012),
    Order(id_order=123456793, id_customer="1234567890", id_serv=67890123),
    Order(id_order=141325379, id_customer="4567891230", id_serv=9382643)]

insertOrder2 = [
    Payment (id_pay=123456, id_order=123456789, name_pay="pix", portion=12),
    Payment(id_pay=123457, id_order=123456790, name_pay="boleto", portion=6),
    Payment(id_pay=123458, id_order=123456791, name_pay="cartão de crédito", portion=3),
    Payment(id_pay=123459, id_order=123456792, name_pay="transferência bancária", portion=4),
    Payment(id_pay=123460, id_order=123456793, name_pay="cheque", portion=2),
    Payment(id_pay=937362, id_order=141325379, name_pay="pix", portion=0)]

# Inserir
 
# session.add_all(insert_customer) 
# session.add_all(insert_itens) 
# session.add_all(insert_orderItens) 
# session.add_all(insertEmployee) 
# session.add_all(insertOrder) 
# session.add_all(insertOrder2)

session.commit()

queryFe = session.query(Customer).all()
queryS = session.query(Item).all()
queryB = session.query(Order_item).all()
queryL = session.query(Employee).all()
queryP = session.query(Order).all()
queryP2 = session.query(Payment).all()

listaQuery = [ queryFe, queryS, queryB, queryL, queryP, queryP2]
listaNomes_print = ['Customers', 'Item', 'Order_item', 'Employee', 'Order', 'Payment']   #ideia doida fernanda as 01:47 da manha ignore
f=0
for a in listaQuery:
    print(f'''
    -----> {listaNomes_print[f]} <-----''')
    f+=1
    for i in a:
        print(f"{i}")
     

session.commit()


# '----> UPDATE <----'
# session.query(Customer).filter(Customer.id_customer == "21499845678").update( { "name_customer" : "Fernanda Cavali"})
# session.query(Item).filter(Item.id_item == 22).update( { "name_item_pedido" : "Cabo de vela"})
# session.query(Item_pedido).filter(Item_pedido.id_item == 22).update( { "service" : "vela ruim"})
# session.query(Order).filter(Order.id_order == 12345678910).update( { "id_customer" : "87332199021"})
# session.query(Payment).filter(Payment.id_pay == 123456).update( { "name_pay" : "cartão"})

# session.commit()

# # # '----> DELETE <----'

# # # session.query(Customer).filter(Customer.id_customer == "21499845678").delete()
# # # session.query(Item).filter(Item.id_item == 22).delete()
# # # session.query(Item_pedido).filter(Item_pedido.id_item == 22).delete()

# Fechar conexão
session.close()  
