from fastapi import status
from src.utils.dependencies import obter_utilizador_atual
from src.main import app
from src.models.cliente_model import Cliente
from src.models.servico_model import Servico

def override_obter_utilizador_atual():
    return {"sub": "utilizador_teste@barber.com"}

@app.on_event("startup")
def setup_auth_override():
    app.dependency_overrides[obter_utilizador_atual] = override_obter_utilizador_atual

def test_raiz_api(client):
    """Testa se a API responde corretamente"""
    response = client.get("/docs")
    assert response.status_code == status.HTTP_200_OK

def test_criar_agendamento(client, db):
    """Testa a criação bem-sucedida de um agendamento"""
    # Criar dados fictícios na BD de teste para satisfazer as chaves estrangeiras
    cliente_teste = Cliente(nome="Cliente Teste", telemovel="912345678")
    servico_teste = Servico(nome="Corte de Cabelo", preco=15.00)
    
    db.add(cliente_teste)
    db.add(servico_teste)
    db.commit()
    db.refresh(cliente_teste)
    db.refresh(servico_teste)
    
    # Dados para o pedido POST
    payload = {
        "cliente_id": cliente_teste.id,
        "servico_id": servico_teste.id,
        "data_hora": "2026-10-10T10:00:00"
    }
    
    response = client.post("/agendamentos/", json=payload)
    
    assert response.status_code == status.HTTP_201_CREATED
    dados_resposta = response.json()
    assert dados_resposta["cliente_id"] == cliente_teste.id
    assert dados_resposta["servico_id"] == servico_teste.id