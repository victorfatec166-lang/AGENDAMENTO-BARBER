from pydantic import BaseModel

class ServicoCreate(BaseModel):
    nome: str
    preco: float
    duracao_min: int = 30

class ServicoResponse(BaseModel):
    id: int
    nome: str
    preco: float
    duracao_min: int

    class Config:
        from_attributes = True