from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from datetime import datetime

from src.config.database import SessionLocal
from src.models.agendamento import AgendamentoModel
from src.models.cliente import ClienteModel
from src.models.barbeiro import BarbeiroModel
from src.models.servico import ServicoModel

router = APIRouter(prefix="/api/agendamentos", tags=["Agendamentos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class AgendamentoCreate(BaseModel):
    cliente_id: int
    barbeiro_id: int
    servico_id: int
    data_hora: datetime

@router.get("/", response_model=List[dict])
def listar_agendamentos(db: Session = Depends(get_db)):
    agendamentos = db.query(AgendamentoModel).all()
    resultado = []
    for a in agendamentos:
        resultado.append({
            "id": a.id,
            "cliente": a.cliente.nome if a.cliente else "Desconhecido",
            "barbeiro": a.barbeiro.nome if a.barbeiro else "Desconhecido",
            "servico": a.servico.nome if a.servico else "Desconhecido",
            "preco": a.servico.preco if a.servico else 0,
            "data_hora": a.data_hora.strftime("%Y-%m-%d %H:%M"),
            "status": a.status
        })
    return resultado

@router.post("/", status_code=201)
def criar_agendamento(agendamento: AgendamentoCreate, db: Session = Depends(get_db)):
    # Valida se cliente, barbeiro e serviço existem
    if not db.query(ClienteModel).filter(ClienteModel.id == agendamento.cliente_id).first():
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    if not db.query(BarbeiroModel).filter(BarbeiroModel.id == agendamento.barbeiro_id).first():
        raise HTTPException(status_code=404, detail="Barbeiro não encontrado")
    if not db.query(ServicoModel).filter(ServicoModel.id == agendamento.servico_id).first():
        raise HTTPException(status_code=404, detail="Serviço não encontrado")

    novo = AgendamentoModel(**agendamento.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return {"mensagem": "Agendamento criado com sucesso!", "id": novo.id}