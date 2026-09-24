from sqlalchemy import Column, Integer, String, Float
from config.database import Base

class ServicoModel(Base):
    __tablename__ = "servicos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    duracao_minutos = Column(Integer, nullable=False)