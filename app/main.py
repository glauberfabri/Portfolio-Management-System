from fastapi import FastAPI
from app.views import router
from app.config import setup_logging

setup_logging()
app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Portfolio Management System"}