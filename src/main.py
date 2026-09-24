from fastapi import FastAPI
from config.database import engine, Base
from models.cliente import ClienteModel
from models.servico import ServicoModel
from models.agendamento import AgendamentoModel
from models.usuario import UsuarioModel
from routers.cliente_router import router as cliente_router
from routers.servico_router import router as servico_router
from routers.agendamento_router import router as agendamento_router
from routers.auth_router import router as auth_router  # <- Adicionado

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(cliente_router)
app.include_router(servico_router)
app.include_router(agendamento_router)
app.include_router(auth_router)  # <- Adicionado

@app.get("/")
def home():
    return {"mensagem": "Sistema de agendamento rodando com sucesso!"}