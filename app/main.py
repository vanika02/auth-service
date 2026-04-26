from fastapi import FastAPI
from app.routers import users
from app.db.db import engine
from app.models import users_model

app = FastAPI(
    title="Auth Serice",
    version="1.0.0",
    description="Authentication microservice using FastAPI"
)

users_model.Base.metadata.create_all(bind=engine)

@app.get("/")
def health_check():
    return {"message": "Auth Service Running "}