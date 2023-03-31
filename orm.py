from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite+pysqlite:///database.db", echo=True)

Session = sessionmaker(bind=engine, autoflush=True)

db = Session()

base = declarative_base()

class Game(base):

    __tablename__ = 'games'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    console = Column(String)
    price = Column(Integer)
    quantity = Column(Integer)

    def __repr__(self):
        return f"Jogo n°{self.id}: {self.name} para {self.console}. R${self.price}, {self.quantity} unidades disponíveis."


base.metadata.create_all(engine)