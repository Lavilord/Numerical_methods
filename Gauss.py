import numpy as np

A = np.array([[8.3, 2.68, 4.1, 1.9, -10.01], [3.92, 8.45, 7.72, 2.46, 12.21], [3.77, 7.27, 8.04, 2.28, 14.81],
              [2.21, 3.59, 1.69, 6.69, -8.35]])
B = np.array([0, 1, 2, 3])

V = A
P = B
n = len(B)
X = np.zeros(n)

counter = 0
for i in range(n):
    max = abs(V[i][counter])
    for j in range (counter,n):
        if abs(V[i][j]) > max:
            max = abs(V[i][j])
            index = j

    if max > abs(V[i][counter]):
        k = B[counter]
        B[counter] = index
        B[index] = k
        for h in range(n):
            value = V[h][counter]
            V[h][counter] = V[h][index]
            V[h][index] = value
    counter += 1
    for j in range(i + 1, n):

        ratio = V[j][i] / V[i][i]

        for k in range(n + 1):
            V[j][k] = V[j][k] - ratio * V[i][k]
        print(V)



X[B[n-1]] = V[n-1][n]/V[n-1][n-1]


for i in range(n - 2, -1, -1):
    X[B[i]] = V[i][n]

    for j in range(i + 1, n):
        X[B[i]] = X[B[i]] - V[i][j] * X[B[j]]

    X[B[i]] = X[B[i]] / V[i][i]
print(X)
