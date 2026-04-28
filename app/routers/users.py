from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.models.users_model import User
from app.schemas.user_schema import (
    UserCreate,
    UserLogin,
    UserResponse
)
from app.auth.auth import (
    hash_password,
    verify_password,
    created_access_token,
    decode_access_token
)

router = APIRouter(prefix="/users", tags=["users"])