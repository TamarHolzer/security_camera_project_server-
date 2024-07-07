# Inequality constraint function
import pulp

# מבטיח שכל מטרה מכוסה במצלמה אחת לפחות אם y[k]היא 1.
def inequality_constraint1(prob, x, y, v, NC, NhD, NvD, NE, NA, NT):
    for k in range(NT):
        prob += pulp.lpSum(v[i][j][d][e][t][k] * x[i, j, d, e, t] for i in range(NC) for j in range(NhD)
                           for d in range(NvD) for e in range(NE) for t in range(NA)) >= y[k]
