from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel

from src.config.database import SessionLocal
from src.models.barbeiro import BarbeiroModel

router = APIRouter(prefix="/api/barbeiros", tags=["Barbeiros"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class BarbeiroCreate(BaseModel):
    nome: str
    telefone: str = None

@router.get("/", response_model=List[dict])
def listar_barbeiros(db: Session = Depends(get_db)):
    barbeiros = db.query(BarbeiroModel).all()
    return [{"id": b.id, "nome": b.nome, "telefone": b.telefone, "ativo": b.ativo} for b in barbeiros]

@router.post("/", status_code=201)
def criar_barbeiro(barbeiro: BarbeiroCreate, db: Session = Depends(get_db)):
    novo = BarbeiroModel(**barbeiro.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return {"mensagem": "Barbeiro registado com sucesso!", "id": novo.id}