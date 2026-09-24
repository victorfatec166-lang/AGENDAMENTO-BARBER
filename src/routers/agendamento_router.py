from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.database import get_db
from models.agendamento import AgendamentoModel as Agendamento
from models.cliente import ClienteModel as Cliente        # <- Com alias
from models.servico import ServicoModel as Servico        # <- Com alias
from schemas.agendamento_schema import AgendamentoCreate, AgendamentoResponse
from utils.dependencies import obter_utilizador_atual

router = APIRouter(prefix="/agendamentos", tags=["Agendamentos"])

@router.post("/", response_model=AgendamentoResponse, status_code=status.HTTP_201_CREATED)
def criar_agendamento(
    agendamento: AgendamentoCreate,
    db: Session = Depends(get_db),
    utilizador_atual = Depends(obter_utilizador_atual)
):
    
    # 1. Verificar se o cliente existe
    cliente_existe = db.query(Cliente).filter(Cliente.id == agendamento.cliente_id).first()
    if not cliente_existe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="O cliente especificado não foi encontrado."
        )

    # 2. Verificar se o serviço existe
    servico_existe = db.query(Servico).filter(Servico.id == agendamento.servico_id).first()
    if not servico_existe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="O serviço especificado não foi encontrado."
        )

    # 3. Verificar se já existe um agendamento exatamente para a mesma data e hora
    conflito = db.query(Agendamento).filter(Agendamento.data_hora == agendamento.data_hora).first()
    if conflito:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Já existe um agendamento marcado para este horário."
        )

    # 4. Criar o novo agendamento se todas as validações passarem
    novo_agendamento = Agendamento(
        cliente_id=agendamento.cliente_id,
        servico_id=agendamento.servico_id,
        data_hora=agendamento.data_hora,
        status="Confirmado"
    )
    
    db.add(novo_agendamento)
    db.commit()
    db.refresh(novo_agendamento)
    
    return novo_agendamento
# Cole a função GET exatamente aqui abaixo:
@router.get("/", response_model=list[AgendamentoResponse])
def listar_agendamentos(
    db: Session = Depends(get_db),
    utilizador_atual = Depends(obter_utilizador_atual)
):
    agendamentos = db.query(Agendamento).all()
    return agendamentos

@router.delete("/{agendamento_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_agendamento(
    agendamento_id: int,
    db: Session = Depends(get_db),
    utilizador_atual = Depends(obter_utilizador_atual)
):
    # 1. Procurar o agendamento pelo ID
    agendamento = db.query(Agendamento).filter(Agendamento.id == agendamento_id).first()
    
    # 2. Se não existir, retornar erro 404
    if not agendamento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="O agendamento especificado não foi encontrado."
        )
    
    # 3. Apagar o registo da base de dados
    db.delete(agendamento)
    db.commit()
    
    return None

@router.put("/{agendamento_id}", response_model=AgendamentoResponse)
def atualizar_agendamento(
    agendamento_id: int,
    agendamento_dados: AgendamentoCreate,
    db: Session = Depends(get_db),
    utilizador_atual = Depends(obter_utilizador_atual)
):
    # 1. Procurar o agendamento pelo ID
    agendamento = db.query(Agendamento).filter(Agendamento.id == agendamento_id).first()
    if not agendamento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="O agendamento especificado não foi encontrado."
        )
    
    # 2. Atualizar os dados do agendamento
    agendamento.cliente_id = agendamento_dados.cliente_id
    agendamento.servico_id = agendamento_dados.servico_id
    agendamento.data_hora = agendamento_dados.data_hora
    
    db.commit()
    db.refresh(agendamento)
    
    return agendamento