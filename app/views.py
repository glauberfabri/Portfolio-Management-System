from fastapi import APIRouter, HTTPException
from app.controllers import get_portfolio, create_portfolio

router = APIRouter()

@router.post("/portfolios/")
def create_new_portfolio(name: str, description: str):
    return create_portfolio(name, description)

@router.get("/portfolios/{portfolio_id}")
def fetch_portfolio(portfolio_id: int):
    return get_portfolio(portfolio_id)