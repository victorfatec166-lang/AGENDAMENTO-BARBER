from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel, EmailStr, Field

from src.config.database import SessionLocal
from src.models.cliente import ClienteModel

router = APIRouter(prefix="/api/clientes", tags=["Clientes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ClienteCreate(BaseModel):
    nome: str = Field(..., min_length=3, description="Nome deve ter pelo menos 3 carateres")
    telefone: str = Field(..., description="Número de telemóvel")
    email: EmailStr
    cpf: str = Field(..., description="CPF do cliente")

@router.get("/", response_model=List[dict])
def listar_clientes(db: Session = Depends(get_db)):
    clientes = db.query(ClienteModel).all()
    resultado = []
    for c in clientes:
        resultado.append({
            "id": c.id,
            "nome": c.nome,
            "telefone": c.telefone,
            "email": c.email,
            "cpf": c.cpf
        })
    return resultado

@router.post("/", status_code=201)
def criar_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    if cliente.cpf:
        existente = db.query(ClienteModel).filter(ClienteModel.cpf == cliente.cpf).first()
        if existente:
            raise HTTPException(status_code=400, detail="Já existe um cliente registado com este CPF.")

    novo_cliente = ClienteModel(
        nome=cliente.nome,
        telefone=cliente.telefone,
        email=cliente.email,
        cpf=cliente.cpf
    )
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)
    return {"mensagem": "Cliente criado com sucesso!", "id": novo_cliente.id}

@router.delete("/{cliente_id}", status_code=204)
def remover_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = db.query(ClienteModel).filter(ClienteModel.id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    
    db.delete(cliente)
    db.commit()
    return None