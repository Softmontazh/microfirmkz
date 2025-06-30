# api/main.py

from fastapi import FastAPI
from api.routes import contracts

app = FastAPI(title="MicrofirmKZ API")

app.include_router(contracts.router, prefix="/contracts", tags=["contracts"])
