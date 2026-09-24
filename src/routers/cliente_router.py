from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from models.cliente import ClienteModel
from schemas.cliente_schema import ClienteCreate, ClienteResponse

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.post("/", response_model=ClienteResponse)
def criar_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    # Verifica se o e-mail já existe
    db_cliente = db.query(ClienteModel).filter(ClienteModel.email == cliente.email).first()
    if db_cliente:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado!")
    
    novo_cliente = ClienteModel(
        nome=cliente.nome,
        telefone=cliente.telefone,
        email=cliente.email
    )
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)
    return novo_cliente

@router.get("/", response_model=list[ClienteResponse])
def listar_clientes(db: Session = Depends(get_db)):
    clientes = db.query(ClienteModel).all()
    return clientes