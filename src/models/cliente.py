from sqlalchemy import Column, Integer, String
from src.config.database import Base

class ClienteModel(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    telefone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    cpf = Column(String, unique=True, nullable=True)