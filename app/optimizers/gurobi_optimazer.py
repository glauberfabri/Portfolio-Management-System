from gurobipy import Model, GRB

def optimize_portfolio(weights, returns):
    model = Model("Portfolio Optimization")
    x = model.addVars(len(weights), lb=0, ub=1, name="weights")
    model.setObjective(sum(x[i] * returns[i] for i in range(len(weights))), GRB.MAXIMIZE)
    model.addConstr(sum(x[i] for i in range(len(weights))) == 1, "Budget")
    model.optimize()
    return {i: x[i].X for i in range(len(weights))}