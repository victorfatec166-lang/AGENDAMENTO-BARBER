from pydantic import BaseModel

class ServicoCreate(BaseModel):
    nome: str
    preco: float
    duracao_minutos: int

class ServicoResponse(BaseModel):
    id: int
    nome: str
    preco: float
    duracao_minutos: int

    class Config:
        from_attributes = True