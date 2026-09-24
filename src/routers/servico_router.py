from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from models.servico import ServicoModel
from schemas.servico_schema import ServicoCreate, ServicoResponse

router = APIRouter(prefix="/servicos", tags=["Serviços"])

@router.post("/", response_model=ServicoResponse)
def criar_servico(servico: ServicoCreate, db: Session = Depends(get_db)):
    novo_servico = ServicoModel(
        nome=servico.nome,
        preco=servico.preco,
        duracao_minutos=servico.duracao_minutos
    )
    db.add(novo_servico)
    db.commit()
    db.refresh(novo_servico)
    return novo_servico

@router.get("/", response_model=list[ServicoResponse])
def listar_servicos(db: Session = Depends(get_db)):
    servicos = db.query(ServicoModel).all()
    return servicos