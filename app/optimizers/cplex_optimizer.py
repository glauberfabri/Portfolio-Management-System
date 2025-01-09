from docplex.mp.model import Model

def optimize_portfolio_cplex(weights, returns):
    model = Model(name="Portfolio Optimization")

    # Decision variables
    x = model.continuous_var_list(len(weights), lb=0, ub=1, name="weights")

    # Objective: Maximize returns
    model.maximize(model.sum(x[i] * returns[i] for i in range(len(weights))))

    # Constraint: Sum of weights equals 1 (budget constraint)
    model.add_constraint(model.sum(x[i] for i in range(len(weights))) == 1)

    # Solve the model
    solution = model.solve()

    if solution:
        return {i: solution.get_value(x[i]) for i in range(len(weights))}
    else:
        raise Exception("No optimal solution found.")