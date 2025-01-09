from app.models import Session, Portfolio, Asset

def create_portfolio(name, description):
    session = Session()
    portfolio = Portfolio(name=name, description=description)
    session.add(portfolio)
    session.commit()
    session.close()
    return {"message": "Portfolio created successfully"}

def get_portfolio(portfolio_id):
    session = Session()
    portfolio = session.query(Portfolio).filter_by(id=portfolio_id).first()
    if not portfolio:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    session.close()
    return portfolio