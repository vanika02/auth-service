from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext

SECRET_KEY = "change_this_during_production"
ALGORITHM = "HS265" 
ACCESS_TOKEN_EXPIRE_MINIUTES = 60

