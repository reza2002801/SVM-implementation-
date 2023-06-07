import cvxpy
import numpy as np


m , p = input().split('   ')

m = int(m)
p = int(p)

m_points = []
p_points = []
for i in range(m):
    x, y = input().split('   ')
    m_points.append((float(x), float(y)))
for i in range(p):
    x, y = input().split('   ')
    p_points.append((float(x), float(y)))

print(m_points)