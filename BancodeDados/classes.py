from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

# Configurações da conexão e sessão

engine = create_engine('postgresql://EUFACOPROGRAMA:apXBE4kgASy6@ep-damp-waterfall-38037149.us-east-2.aws.neon.tech/mecanica_teste?sslmode=require')
'''engine = create_engine('postgresql://postgres:pgadmin123@localhost:5432/mecanica_teste')'''
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Entidades
class Customer(Base):
    __tablename__ = 'customer'       #nome da tabela no Banco de Dados

    id_customer = Column(String, primary_key=True)
    number_customer = Column(Integer, nullable=False)
    address_customer = Column(String, nullable=False)
    name_customer = Column(String, nullable=False)
    car = Column(String, nullable=False)

    def __repr__(self):
        return f'Cliente {self.name_customer}, proprietário {self.car}, Cpf: {self.id_customer}, Tel: {self.number_customer}'

class Item(Base):
    __tablename__ = 'item'

    id_item = Column(Integer, primary_key=True)
    name_item_request = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    
    def __repr__(self):
        return f"Número do item: {self.id_item}, nome: {self.name_item_request}, preço: R${self.price} reais"

class Item_pedido(Base):
    __tablename__ = 'item_pedido'

    id_item = Column(Integer, primary_key=True)
    payment = Column(String, nullable=False)
    request = Column(String, nullable=False)
    service = Column(String, nullable=False)
    
    def __repr__ (self):
        return f''' Número do Item: {self.id_item},
        Tipo de pagamento: {self.payment}, 
        Pedido: {self.request}, 
        Serviço: {self.service}'''

class Employee(Base):
    __tablename__ = 'employee'

    id_employee = Column(String, primary_key = True)
    name_employee = Column(String, nullable = False)
    number_employee = Column(Integer, nullable = False)
    adress_employee = Column(String, nullable = False)
    wage_employee = Column(Float, nullable = False)
    date_born = Column(Date, nullable = False)

    def __repr__(self):
        return f''' O funcionario {self.name_employee}, numero {self.number_employee} está responsável pelo serviço'''
    
class Order(Base):
    __tablename__ = 'order_table'

    id_order = Column(Integer, primary_key=True)
    id_customer = Column(String, ForeignKey("customer.id_customer"), nullable=False)
    id_serv = Column(Integer, nullable=False)
    
    def __repr__ (self):
        return f""" Pedido {self.id_order}, quem pediu {self.id_customer}
                id serviço : {self.id_customer} """
    
class Payment(Base):
    __tablename__ = 'payment'

    id_pay = Column(Integer, primary_key=True)
    id_order = Column(Integer, ForeignKey("order_table.id_order"), nullable=False)
    name_pay = Column(String, nullable=False)
    portion = Column(Integer, nullable=False)
    
    def __repr__ (self):
        return f""" Pagamento {self.id_pay}, 
                    forma de pagamento {self.name_pay}
                    Pedido {self.id_order}
                    parcelas: {self.portion} """    


# Criação das tabelas no banco de dados (verifica se existe)
Base.metadata.create_all(engine)

session.commit() #efetivar comando
session.close()  #fechar sessao