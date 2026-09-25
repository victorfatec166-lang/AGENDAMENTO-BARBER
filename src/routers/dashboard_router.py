from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.models.cliente import ClienteModel
from src.models.agendamento import AgendamentoModel

router = APIRouter(prefix="/api/dashboard", tags=["Dashboard"])

@router.get("/stats")
def obter_estatisticas(db: Session = Depends(get_db)):
    # Conta quantos registos existem nas respetivas tabelas da base de dados
    total_clientes = db.query(ClienteModel).count()
    total_agendamentos = db.query(AgendamentoModel).count()
    
    return {
        "agendamentos_hoje": total_agendamentos,
        "clientes_ativos": total_clientes,
        "faturamento_mensal": 12850.00, 
        "servicos_realizados": total_agendamentos
    }