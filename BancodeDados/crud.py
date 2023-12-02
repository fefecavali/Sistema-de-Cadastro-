from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

''' --> Configurações  '''

# engine = create_engine('postgresql://EUFACOPROGRAMA:apXBE4kgASy6@ep-damp-waterfall-38037149.us-east-2.aws.neon.tech/mecanica_teste?sslmode=require')
engine = create_engine('postgresql://postgres:pgadmin123@localhost:5432/')
Session = sessionmaker(bind=engine)
session = Session()
base = declarative_base()


#Entidades
class Customer(base):
    __tablename__ = 'customer'

    id_customer = Column(String, primary_key=True)
    number_customer = Column(Integer, nullable=False)
    address_customer = Column(String, nullable=False)
    name_customer = Column(String, nullable=False)
    car = Column(String, nullable=False)

    def __repr__ (self):
        return f''' Cliente {self.name_customer}, proprietário {self.car} 
        Cpf : {self.id_customer} 
        Tel : {self.number_customer}'''
    
class Item(base):
    __tablename__ = 'item'

    id_item = Column(Integer, primary_key=True)
    name_item_request = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    
    def repr (self):
        return f" número do item: {self.id_item}, nome: {self.name_item_pedido}, preço: R${self.price} reais"

class Item_pedido(base):
    __tablename__ = 'Item_pedido'

    id_item = Column(Integer, primary_key=True)
    payment = Column(String, nullable=False)
    request = Column(String, nullable=False)
    service = Column(String, nullable=False)
    
    def __repr__ (self):
        return f''' Número do Item: {self.id_item},
        Tipo de pagamento: {self.payment}, 
        Pedido: {self.request}, 
        Serviço: {self.service}'''

class employee(base):
    __tablename__ = 'employee'

    id_employee = Column(String, primary_key = True)
    name_employee = Column(String, nullable = False)
    number_employee = Column(Integer, nullable = False)
    adress_employee = Column(String, nullable = False)
    wage_employee = Column(Float, nullable = False)
    date_born = Column(Date, nullable = False)

    def __repr__(self):
        return f''' O funcionario {self.name_employee}, numero {self.number_employee} está responsável pelo serviço'''
    
class Order(base):
    __tablename__ = 'Order'

    id_order = Column(Integer, primary_key=True)
    id_customer = Column(String, ForeignKey("id_customer"), nullable=False)
    id_serv = Column(Integer, nullable=False)
    
    def __repr__ (self):
        return f""" Pedido {self.id_order}, quem pediu {self.id_customer}
                id serviço : {self.id_customer} """
    
class Payment(base):
    __tablename__ = 'Order'

    id_pay = Column(Integer, primary_key=True)
    id_order = Column(Integer, ForeignKey("id_order"), nullable=False)
    name_pay = Column(String, nullable=False)
    portion = Column(Integer, nullable=False)
    
    def __repr__ (self):
        return f""" Pagamento {self.id_pay}, 
                    forma de pagamento {self.name_pay}
                    Pedido {self.id_order}
                    parcelas: {self.portion} """    
#SQL

'----> INSERT <----'

data_insert = Customer ( id_customer="21499845678", number_customer=998058909 ,address_customer="Rua Mambore bonita" ,name_customer="Fernanda", car="Ferrari 2025" )
data_insert = Item ( id_item=22, name_item_request="Vela" ,price=20)
data_insert = Item_pedido ( id_Item=22, payment="dinheiro" ,request="a vista", service="vela queimada")

session.commit()

'----> SELECT <----'

data = session.query(Customer).all()
data = session.query(Item).all()
data = session.query(Item_pedido).all()

session.commit()

'----> UPDATE <----'
session.query(Customer).filter(Customer.id_customer == "21499845678").update( { "name_customer" : "Fernanda Cavali"})
session.query(Item).filter(Item.id_item == 22).update( { "name_item_pedido" : "Cabo de vela"})
session.query(Item_pedido).filter(Item_pedido.id_item == 22).update( { "service" : "vela ruim"})
session.commit()

'----> DELETE <----'

session.query(Customer).filter(Customer.id_customer == "21499845678").delete()
session.query(Item).filter(Item.id_item == 22).delete()
session.query(Item_pedido).filter(Item_pedido.id_item == 22).delete()


session.commit()



session.close()           #Fechar conexão


