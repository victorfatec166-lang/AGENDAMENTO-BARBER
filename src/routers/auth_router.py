from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from config.database import get_db
from models.usuario import UsuarioModel
from schemas.usuario_schema import UsuarioCreate, UsuarioResponse
from utils.security import obter_senha_hash, verificar_senha, criar_token_acesso

router = APIRouter(tags=["Autenticação"])

@router.post("/signup", response_model=UsuarioResponse)
def registar_utilizador(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_existente = db.query(UsuarioModel).filter(UsuarioModel.email == usuario.email).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="Este e-mail já está registado!")
    
    senha_hash = obter_senha_hash(usuario.senha)
    novo_utilizador = UsuarioModel(
        email=usuario.email,
        senha_hash=senha_hash,
        tipo=usuario.tipo
    )
    db.add(novo_utilizador)
    db.commit()
    db.refresh(novo_utilizador)
    return novo_utilizador

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = db.query(UsuarioModel).filter(UsuarioModel.email == form_data.username).first()
    if not usuario or not verificar_senha(form_data.password, usuario.senha_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="E-mail ou palavra-passe incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = criar_token_acesso(data={"sub": usuario.email, "tipo": usuario.tipo})
    return {"access_token": access_token, "token_type": "bearer"}