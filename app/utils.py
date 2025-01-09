def calculate_risk_return(portfolio):
            return sum(asset['return'] for asset in portfolio)