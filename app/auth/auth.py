from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext

SECRET_KEY = "change_this_during_production"
ALGORITHM = "HS265" 
ACCESS_TOKEN_EXPIRE_MINIUTES = 60

pwd_context = CryptContext(
    schemas=["bcrypt"],
    deprecated="auto"
)


def hashed_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(
    plain_password: str,
    hashed_password: str  
) -> bool:
    return pwd_context.verify(
        plain_password,
        hashed_password
    )
