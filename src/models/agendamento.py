from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from config.database import Base
from datetime import datetime

class AgendamentoModel(Base):
    __tablename__ = "agendamentos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    servico_id = Column(Integer, ForeignKey("servicos.id"), nullable=False)
    data_hora = Column(DateTime, nullable=False, default=datetime.utcnow)
    status = Column(String, default="confirmado")