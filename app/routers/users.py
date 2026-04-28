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

@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )
    
    new_user = User(
        username=user.username,
        email=user.email,
        hash_password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully"}