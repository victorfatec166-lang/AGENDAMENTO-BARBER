import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy.orm import Session

from src.config.database import SessionLocal, engine, Base
from src.models.usuario import UsuarioModel
from src.models.cliente import ClienteModel
from src.models.barbeiro import BarbeiroModel
from src.models.servico import ServicoModel
from src.utils.security import obter_senha_hash

# Importação dos Routers
from src.routers.cliente_router import router as cliente_router
from src.routers.servico_router import router as servico_router
from src.routers.agendamento_router import router as agendamento_router
from src.routers.dashboard_router import router as dashboard_router
from src.routers.auth_router import router as auth_router

load_dotenv()

app = FastAPI(
    title="Sovereign Barber Studio",
    description="Sistema de Gestão e Agendamentos",
    version="1.0.0"
)

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

Base.metadata.create_all(bind=engine)

def criar_admin_inicial():
    db: Session = SessionLocal()
    admin_email = os.getenv("ADMIN_EMAIL", "admin@sovereign.com")
    admin_senha = os.getenv("ADMIN_SENHA", "123456")

    usuario_existente = db.query(UsuarioModel).filter(UsuarioModel.email == admin_email).first()
    if not usuario_existente:
        senha_criptografada = obter_senha_hash(admin_senha)
        novo_admin = UsuarioModel(
            email=admin_email,
            senha_hash=senha_criptografada,
            is_admin=True
        )
        db.add(novo_admin)
        db.commit()
        print(">>> Administrador criado com segurança na base de dados!")
    db.close()

@app.on_event("startup")
def criar_dados_iniciais():
    criar_admin_inicial()
    db: Session = SessionLocal()
    try:
        if db.query(ClienteModel).count() == 0:
            db.add(ClienteModel(nome="Carlos Silva", telefone="912345678", email="carlos@email.com"))
            db.add(BarbeiroModel(nome="João Master", telefone="987654321"))
            db.add(ServicoModel(nome="Corte Degradê", descricao="Corte moderno com navalha", preco=15.00, duracao_minutos=30))
            db.commit()
            print(">>> Dados de teste criados com sucesso!")
    finally:
        db.close()

# Registar os Routers
app.include_router(cliente_router)
app.include_router(servico_router)
app.include_router(agendamento_router)
app.include_router(dashboard_router)
app.include_router(auth_router)

@app.get("/")
def raiz():
    return RedirectResponse(url="/static/login.html")

@app.get("/api/health")
def health_check():
    return {"status": "online", "mensagem": "Sistema de agendamento rodando com sucesso!"}