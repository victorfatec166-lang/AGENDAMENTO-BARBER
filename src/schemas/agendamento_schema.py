from pydantic import BaseModel
from datetime import datetime

class AgendamentoCreate(BaseModel):
    cliente_id: int
    servico_id: int
    data_hora: datetime

class AgendamentoResponse(BaseModel):
    id: int
    cliente_id: int
    servico_id: int
    data_hora: datetime
    status: str

    class Config:
        from_attributes = True