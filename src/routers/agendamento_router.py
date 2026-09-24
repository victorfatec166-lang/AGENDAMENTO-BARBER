from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta
from config.database import get_db
from models.agendamento import AgendamentoModel
from models.cliente import ClienteModel
from models.servico import ServicoModel
from models.usuario import UsuarioModel
from schemas.agendamento_schema import AgendamentoCreate, AgendamentoResponse
from utils.dependencies import obter_utilizador_atual  # <- Importação da segurança

router = APIRouter(prefix="/agendamentos", tags=["Agendamentos"])

@router.post("/", response_model=AgendamentoResponse)
def criar_agendamento(
    agendamento: AgendamentoCreate, 
    db: Session = Depends(get_db),
    utilizador_atual: UsuarioModel = Depends(obter_utilizador_atual) # <- Rota protegida!
):
    # 1. Verifica se o cliente existe
    cliente = db.query(ClienteModel).filter(ClienteModel.id == agendamento.cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado!")
    
    # 2. Verifica se o serviço existe e obtém a sua duração
    servico = db.query(ServicoModel).filter(ServicoModel.id == agendamento.servico_id).first()
    if not servico:
        raise HTTPException(status_code=404, detail="Serviço não encontrado!")

    # 3. Validação de Conflito de Horário
    inicio_novo = agendamento.data_hora
    fim_novo = inicio_novo + timedelta(minutes=servico.duracao_minutos)

    agendamentos_existentes = db.query(AgendamentoModel).all()
    
    for ag in agendamentos_existentes:
        servico_existente = db.query(ServicoModel).filter(ServicoModel.id == ag.servico_id).first()
        inicio_existente = ag.data_hora
        fim_existente = inicio_existente + timedelta(minutes=servico_existente.duracao_minutos)

        if inicio_novo < fim_existente and fim_novo > inicio_existente:
            raise HTTPException(
                status_code=400, 
                detail="Horário indisponível! Já existe um agendamento neste intervalo."
            )

    # 4. Cria o agendamento associado ao utilizador autenticado (opcional, se quiser guardar quem criou)
    novo_agendamento = AgendamentoModel(
        cliente_id=agendamento.cliente_id,
        servico_id=agendamento.servico_id,
        data_hora=agendamento.data_hora,
        status="confirmado"
    )
    db.add(novo_agendamento)
    db.commit()
    db.refresh(novo_agendamento)
    return novo_agendamento

@router.get("/", response_model=list[AgendamentoResponse])
def listar_agendamentos(db: Session = Depends(get_db)):
    agendamentos = db.query(AgendamentoModel).all()
    return agendamentos