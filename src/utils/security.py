from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt
from src.config.settings import settings  # Importação corrigida com src.

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verificar_senha(senha_plain: str, senha_hash: str) -> bool:
    return pwd_context.verify(senha_plain, senha_hash)

def obter_senha_hash(senha: str) -> str:
    return pwd_context.hash(senha)

def criar_token_acesso(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    # Usando os valores protegidos pelas definições e variáveis de ambiente
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt