from pydantic import BaseModel
from typing import Optional

class ClienteCreate(BaseModel):
    nome: str
    telefone: str
    email: Optional[str] = None  # Opcional, caso queira guardar o email futuramente

class ClienteResponse(BaseModel):
    id: int
    nome: str
    telefone: str
    email: Optional[str] = None

    class Config:
        from_attributes = True