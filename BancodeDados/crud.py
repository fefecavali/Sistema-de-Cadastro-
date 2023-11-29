from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Configurações
engine = create_engine('postgresql://postgres:pgadmin123@localhost:5432/mecanica_teste')

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
        return f" Cliente {self.name_customer}, proprietário {self.car}
                Cpf : {self.id_customer} 
                Tel : {self.number_customer}"
    
#SQL

## ----> INSERT <----
data_insert = Customer ( id_customer="21499845678", number_customer=998058909 ,address_customer="Rua Mambore bonita" ,name_customer="Fernanda", car="Ferrari 2025" )
session.commit()

## ----> SELECT <----
data = session.query(Customer).all()
session.commit()

## ----> UPDATE <----
session.query(Customer).filter(Customer.id_customer == "21499845678").update( { "name_customer" : "Fernanda Cavali"})
session.commit()

## ----> DELETE <----
# session.query(Customer).filter(Customer.id_customer ==="21499845678").delete()
# session.commit()


session.close()           #Fechar conexão

