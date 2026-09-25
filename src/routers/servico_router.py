from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel

from src.config.database import SessionLocal
from src.models.servico import ServicoModel

router = APIRouter(prefix="/api/servicos", tags=["Serviços"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ServicoCreate(BaseModel):
    nome: str
    descricao: str = None
    preco: float
    duracao_minutos: int = 30

@router.get("/", response_model=List[dict])
def listar_servicos(db: Session = Depends(get_db)):
    servicos = db.query(ServicoModel).all()
    return [{"id": s.id, "nome": s.nome, "descricao": s.descricao, "preco": s.preco, "duracao_minutos": s.duracao_minutos} for s in servicos]

@router.post("/", status_code=201)
def criar_servico(servico: ServicoCreate, db: Session = Depends(get_db)):
    novo = ServicoModel(**servico.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return {"mensagem": "Serviço criado com sucesso!", "id": novo.id}