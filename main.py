from fastapi import FastAPI
from app.api.routes import health, auth

app = FastAPI(title="FastAPI Boilerplate")

app.include_router(health.router)
app.include_router(auth.router, prefix="/auth")
