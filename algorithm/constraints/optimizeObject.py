import pulp


def objective_function(prob, x, NC, NhD, NvD, NE, NA):
    prob += pulp.lpSum(x[(i, j, d, e, t)]
                       for i in range(NC)
                       for j in range(NhD)
                       for d in range(NvD)
                       for e in range(NE)
                       for t in range(NA)), "Minimize number of cameras"
