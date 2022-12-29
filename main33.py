import numpy as np
import cvxpy as cp
import math

endpoints_set = [
    [[0,0],[1,5]],
    [[2,4],[5,4]],
    [[1,4],[4,-4]],
    [[-10,4],[5,-5]]
]
v1 = np.array([0,0])
v2 = np.array([1,5])
v3 = np.array([2,4])
v4 = np.array([5,4])
v5 = np.array([1,4])
v6 = np.array([4, -4])
v7 = np.array([10,4])
v8 = np.array([5,-5])

endpoint = [-15, -45]


#declaring my variables
alph1 = cp.Variable()
beta1 = cp.Variable()
point1 = [alph1, beta1]

alph2 = cp.Variable()
beta2 = cp.Variable()
point2 = [alph2, beta2]

alph3 = cp.Variable()
beta3 = cp.Variable()
point3 = [alph3, beta3]

alph4 = cp.Variable()
beta4 = cp.Variable()
point4 = [alph4, beta4]


funcy = (alph4-alph3)**2 + (alph3-alph2)**2 + (alph2-alph1)**2 + (endpoint[0]-alph4)**2 + (beta4-beta3)**2 + (beta3-beta2)**2 + (beta2-beta1)**2 + (endpoint[1]-beta4)**2

function = math.sqrt(funcy)

obj = cp.Minimize(function)

def isBetween(a, b, c):
    crossproduct = (c[1] - a[1]) * (b[0] - a[0]) - (c[0] - a[0]) * (b[1] - a[1])

    if abs(crossproduct) >= 0:
        return False

    dotproduct = (c[0] - a[0]) * (b[0] - a[0]) + (c[1] - a[1])*(b[1] - a[1])
    if dotproduct < 0:
        return False

    squaredlengthba = (b[0] - a[0])*(b[0] - a[0]) + (b[1] - a[1])*(b[1] - a[1])
    if dotproduct > squaredlengthba:
        return False

    return True


constraints = [isBetween(endpoints_set[0][0], endpoints_set[0][1], point1) == True, isBetween(endpoints_set[1][0], endpoints_set[1][1], point2) == True, isBetween(endpoints_set[2][0], endpoints_set[2][1], point3) == True, isBetween(endpoints_set[3][0], endpoints_set[3][1], point4) == True]


problem = cp.Problem(obj, constraints)
problem.solve()

print("status: ", problem.status)
print("optimal values: ", problem.value)
print("optimal vars: ", alph1, beta1, alph2, beta2, alph3, beta3, alph4, beta4)
