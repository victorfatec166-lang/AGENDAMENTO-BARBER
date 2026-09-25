from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
from src.config.database import Base
from src.models.cliente import ClienteModel
from src.models.barbeiro import BarbeiroModel
from src.models.servico import ServicoModel

class AgendamentoModel(Base):
    __tablename__ = "agendamentos"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    barbeiro_id = Column(Integer, ForeignKey("barbeiros.id"), nullable=False)
    servico_id = Column(Integer, ForeignKey("servicos.id"), nullable=False)
    data_hora = Column(DateTime, nullable=False)
    status = Column(String, default="Pendente")

    cliente = relationship("ClienteModel")
    barbeiro = relationship("BarbeiroModel")
    servico = relationship("ServicoModel")