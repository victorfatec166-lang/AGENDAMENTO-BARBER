from pydantic import BaseModel, EmailStr

class UsuarioCreate(BaseModel):
    email: EmailStr
    senha: str
    tipo: str = "cliente"

class UsuarioResponse(BaseModel):
    id: int
    email: str
    tipo: str

    class Config:
        from_attributes = True