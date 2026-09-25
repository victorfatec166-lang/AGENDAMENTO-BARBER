from pydantic import BaseModel

class AgendamentoCreate(BaseModel):
    cliente_id: int
    servico_id: int
    data_hora: str

class AgendamentoResponse(BaseModel):
    id: int
    cliente_id: int
    servico_id: int
    data_hora: str
    status: str

    class Config:
        from_attributes = True