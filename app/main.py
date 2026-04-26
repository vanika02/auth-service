from fastapi import FastAPI
from app.routers import users


app = FastAPI(
    title="Auth Serice",
    version="1.0.0",
    description="Authentication microservice using FastAPI"
)

app.include_router(users.router)

@app.get("/")
def health_check():
    return {"message": "Auth Service Running "}