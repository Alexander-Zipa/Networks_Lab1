import scipy as sp
from scipy import linalg

n = 1000
A = sp.zeros((n, n))
p = 0.7
R = 100  # resistance of single edge
i, j = 0, 0
for i in range(0, n):
    for j in range(i + 1, n):
        A[i][j] = (sp.rand() < p)
        A[j][i] = A[i][j]
k = sp.sum(A, 1)
L = sp.diag(k) - A
i, j = 147, 366  # nodes to measure resistance
I = sp.zeros(n)
I[i] = 1
I[j] = -1
I1 = sp.delete(I, j)
L1 = sp.delete(L, j, 0)
L1 = sp.delete(L1, j, 1)
if abs(linalg.det(L1)) > 10 ** -6:
    V1 = R * sp.dot(linalg.inv(L1), I1)
    V = sp.insert(V1, j, [0])
    print('Resistance between nodes ', i, ' and ', j, ':')
    print(abs((V[i]-V[j])/I[i]))
else:
    print('Matrix is singular')
