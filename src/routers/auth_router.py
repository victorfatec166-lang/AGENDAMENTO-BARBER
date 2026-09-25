from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr

from src.config.database import get_db
from src.models.usuario import UsuarioModel
from src.utils.security import verificar_senha, criar_token_acesso

router = APIRouter(prefix="/api/auth", tags=["Autenticação"])

class LoginSchema(BaseModel):
    email: EmailStr
    senha: str

@router.post("/login")
def login(dados: LoginSchema, db: Session = Depends(get_db)):
    # Procura o utilizador pelo e-mail na base de dados
    usuario = db.query(UsuarioModel).filter(UsuarioModel.email == dados.email).first()
    
    # Valida se o utilizador existe e se a senha está correta
    if not usuario or not verificar_senha(dados.senha, usuario.senha_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="E-mail ou palavra-passe incorretos."
        )
    
    # Gera o token JWT de acesso
    access_token = criar_token_acesso(data={"sub": usuario.email})
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }