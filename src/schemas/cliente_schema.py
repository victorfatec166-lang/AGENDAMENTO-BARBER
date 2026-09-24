from pydantic import BaseModel

class ClienteCreate(BaseModel):
    nome: str
    telefone: str
    email: str

class ClienteResponse(BaseModel):
    id: int
    nome: str
    telefone: str
    email: str

    class Config:
        from_attributes = True