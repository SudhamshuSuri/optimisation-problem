import numpy as np
import matplotlib.pyplot as plt
a = np.array((-9.09000000000001, 3.79000000000000))
b = np.array((-5.27000000000001, 5.37000000000001))
c = np.array((-8.15000000000001, 1.31000000000000))
d = np.array((-4.00000000000000, 3.00000000000000))
e = np.array((-5.43000000000001, -1.81000000000000))
f = np.array((-2.05000000000000, 0.450000000000001))
g = np.array((-2.23000000000000, -3.73000000000000))
h = np.array((2.95000000000000, -2.69000000000000))
m = [0.4136125654450287, 0.4072289156626497, 0.6686390532544361, 0.2007722007722008]
intercept = [7.549738219895316, 4.6289156626505985, 1.8207100591715948, -3.2822779922779923]


pointsetlist = [[a,b], [c,d], [e,f], [g,h]]

##RHS MATRIX##
C = np.zeros(4)

C[0] = h[0] +m[0]*h[1] - 2*intercept[0]*m[0] + m[0]*intercept[1]
C[-1] = -m[-1]*intercept[-2] + m[-1]*intercept[-1]

for i in range(1,4):
    C[i] = 2*m[i-1]*intercept[i-1] -m[i-2]*intercept[i-1] - m[i-2]*intercept[i-1]

#print(f"C = {C}")

##LHS TRI-DIAG MATRIX###

A = np.zeros((4,4))

for i in range(4):
    try:
        A[i][i] = -2*(1 + m[i]**2)
        A[i][i-1] = 1 + m[i]*m[i-1]
        A[i-1][i] = A[i][i-1]
        A[3][0] = A[0][3] = 0
    except IndexError:
        pass 

#print(f"A = {A}")

##final-ans##
ans = np.dot(C, np.linalg.inv(A))


##generating a,b pairs

bmat = np.zeros(4)
for i in range(0, len(ans)):
    bmat[i] = m[i]*ans[i] + intercept[i]

#print(bmat)

pointplot = [(x,y) for (x,y) in zip(ans, bmat)]

print(pointplot)

#ifpoint is outside the line force it to the nearest point on the line segment

def LineFit(point1, point2, point3):
    min_values = np.minimum(point1, point2)
    max_values = np.maximum(point1, point2)

    between = np.all((point3 >= min_values) & (point3 <= max_values), axis=0)   

    if between:
        return point3
    else:
        distance1 = np.linalg.norm(point3 - point1)
        distance2 = np.linalg.norm(point3 - point2)
    
        if distance1 <= distance2:
            return point1
        else:
            return point2


x = [a[0], b[0], c[0], d[0], e[0], f[0], g[0]]

y = [a[1], b[1], c[1], d[1], e[1], f[1], g[1]]

pointplotfinal = [0,0,0,0]

for i in range(0,4):
    pointplotfinal[i] = np.array(LineFit(pointsetlist[i][0], pointsetlist[i][1], pointplot[i]))



plt.scatter(x,y, color='g')
plt.plot(pointplotfinal, color='y') 
plt.show()
