from sqlalchemy import Column, Integer, String, Float
from src.config.database import Base

class ServicoModel(Base):
    __tablename__ = "servicos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    preco = Column(Float, nullable=False)
    duracao_minutos = Column(Integer, default=30)