from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pathlib import Path

# Inicialização da aplicação FastAPI
app = FastAPI(
    title="Sovereign Barber Studio",
    description="Sistema de Gestão e Agendamentos",
    version="1.0.0"
)

# Definição segura dos diretórios base e estáticos (pasta src/static)
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"

# Montagem correta da pasta estática
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# Tentar incluir os routers (com proteção caso algum ficheiro ainda não exista)
try:
    from src.routers.cliente_router import router as cliente_router
    from src.routers.servico_router import router as servico_router
    from src.routers.agendamento_router import router as agendamento_router
    from src.routers.auth_router import router as auth_router

    app.include_router(cliente_router)
    app.include_router(servico_router)
    app.include_router(agendamento_router)
    app.include_router(auth_router)
except ImportError:
    pass

# Rota Raiz: Redireciona para o login estático
@app.get("/")
def raiz():
    return RedirectResponse(url="/static/login.html")

# Rota de verificação de saúde da API
@app.get("/api/health")
def health_check():
    return {"status": "online", "mensagem": "Sistema de agendamento rodando com sucesso!"}