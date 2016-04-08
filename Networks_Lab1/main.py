import scipy as sp
from scipy import linalg
from scipy import sparse
import time

start_time = time.time()
n = 1000
A = sp.zeros((n, n))
p = 0.7
R = 100  # resistance of single edge
i, j = 0, 0
for i in range(0, n):
    for j in range(i + 1, n):
        A[i][j] = (sp.rand() < p)
        A[j][i] = A[i][j]
A = sparse.csr_matrix(A)
k = sparse.csr_matrix(A.sum(axis=1))
L = sparse.csr_matrix(sp.diag(k.toarray()[:, 0]) - A)
i, j = 147, 366  # nodes to measure resistance
I = sp.zeros(n)
I[i] = 1
I[j] = -1
I = sparse.csr_matrix(I).transpose()
I1 = sparse.csr_matrix(sp.delete(I.toarray(), j, 0))
L1 = sparse.csr_matrix(sp.delete(L.toarray(), j, 0))
L1 = sparse.csr_matrix(sp.delete(L1.toarray(), j, 1))
if abs(linalg.det(L1.toarray())) > 10 ** -6:
    V1 = sparse.csr_matrix(R * linalg.inv(L1.toarray()) * I1)
    V = sparse.csr_matrix(sp.insert(V1.toarray(), j, [0])).transpose()
    print('Resistance between nodes ', i, ' and ', j, ':')
    print(abs((V[i, 0] - V[j, 0])/I[i, 0]))
else:
    print('Matrix is singular')
end_time = time.time()
print('Elapsed time:', end_time - start_time)
