import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt

white , black = input().strip().split('   ')

white = int(white)
black = int(black)

white_points = []
black_points = []

for i in range(white):
    x, y = input().strip().split('   ')
    white_points.append((float(x), float(y)))
for i in range(black):
    x, y = input().strip().split('   ')
    black_points.append((float(x), float(y)))



m = white + black
n = 2


c = np.array([0,1]).astype(np.float32)




A = np.random.randn(m, n)
y = np.random.randn(m)
for i in range(white):
    y[i] = 1
    A[i, 0] =  white_points[i][0]
    A[i, 1] =  white_points[i][1]
for i in range( black):
    y[i] = -1
    A[i + white, 0] = black_points[i][0]
    A[i + white, 1] = black_points[i][1]


b = cp.Variable()
w = cp.Variable(n)

v = np.ones(m)

x_constraints = [w @ A[i] + b >= 1  for i in range(white)]
y_constraints = [w @ A[i+white] + b <= -1 for i in range(black)]


constraints = x_constraints +  y_constraints

c = np.array([0,1])
objective = cp.Minimize(c @ w)

prob = cp.Problem(objective,constraints)

prob.solve()




plt.axline((0,(-1*b.value-(w.value[0]*0))/w.value[1]),(1 ,(-1*b.value-(w.value[0]*1))/w.value[1]))
s1 = ((-1*b.value-(w.value[0]*1))/w.value[1])-(-1*b.value-(w.value[0]*0))/w.value[1]
s2 = ((-1*b.value-(w.value[0]*0))/w.value[1])
print(f'({s1},{s2})')





# plt.scatter(A[:white,0],A[:white,1],color = 'red')
# plt.scatter(A[white:,0],A[white:,1],color = 'green')
# plt.show()



