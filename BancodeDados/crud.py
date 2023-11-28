from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
import psycopg2

engine = create_engine('postgresql://postgres:pgadmin123@localhost:5432/mecanica_teste')

Session = sessionmaker(bind=engine)
session = Session()
base = declarative_base()

class Pecas(base):
    __tablename__ = 'pecas'

    nome = Column(String, primary_key=True)
    preco = Column(Integer, nullable=False)

    def __repr__ (self):
        return f'oi'

peca1 = Pecas(nome='Valmir', preco=100)

session.add(peca1)
session.commit()

# consulta = session.query(Pecas).all()
# print(consulta[0])

session.close()
