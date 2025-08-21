from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import HTTPException, status

from dotenv import load_dotenv
import os

load_dotenv() 

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})  # adiciona expiração
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  # verifica validade e expiração
        user_id: int = int(payload.get("sub"))
        if user_id is None:
            return None
        return user_id
    except JWTError:
        return None