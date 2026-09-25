from sqlalchemy import Column, Integer, String, Boolean
from src.config.database import Base

class BarbeiroModel(Base):
    __tablename__ = "barbeiros"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    telefone = Column(String, nullable=True)
    ativo = Column(Boolean, default=True)