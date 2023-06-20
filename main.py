from fastapi import FastAPI
from api import base
from fastapi.exceptions import RequestValidationError
import warnings

warnings.filterwarnings("ignore")

app = FastAPI()

app.include_router(base.router)

@app.get("/health")
async def root():
    return {"message": "I am there..."}