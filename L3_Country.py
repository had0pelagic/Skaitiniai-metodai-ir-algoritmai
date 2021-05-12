import numpy as np
import matplotlib.pyplot as plt
import os
import time
import scipy.integrate

plt.style.use('bmh')
os.system("cls")


def Hermite(X, j, x):
    l = Lagrange(X, j, x)
    dl = D_Lagrange(X, j, X[j])
    U = (1 - 2 * dl * (x - X[j])) * l ** 2
    V = (x - X[j]) * l ** 2
    return U, V


def Lagrange(X, j, x):
    l = 1
    for k in range(len(X)):
        if j != k:
            l = l * ((x - X[k]) / (X[j] - X[k]))
    return l


def D_Lagrange(X, j, x):
    dl = 0
    for i in range(len(X)):
        lds = 1
        if i != j:
            for k in range(len(X)):
                if (k != j) and (k != i):
                    lds = lds * (x - X[k])
            dl = dl + lds

    ldv = 1
    for i in range(len(X)):
        if i != j:
            ldv = ldv * (X[j] - X[i])
    dl = dl / ldv
    return dl


def Akima(x, y, i):
    X = x[i]
    if i == len(x)-1:
        i = i-1

    dy1 = (((X - x[i]) + (X - x[i + 1])) /
           ((x[i - 1] - x[i]) * (x[i - 1] - x[i + 1]))) * y[i - 1]

    dy2 = (((X - x[i-1]) + (X - x[i + 1])) /
           ((x[i] - x[i - 1]) * (x[i] - x[i + 1]))) * y[i]

    dy3 = (((X - x[i-1]) + (X - x[i])) /
           ((x[i + 1] - x[i - 1]) * (x[i + 1] - x[i]))) * y[i + 1]

    return dy1 + dy2 + dy3


def Hermite_interpolation(x, y, nv, t):
    plt.scatter(x, y, color="black", s=30)  # normal
    for i in range(0, len(t) - 1):
        nt = np.linspace(t[i], t[i + 1], nv)
        fx = 0
        fy = 0
        for j in range(0, 2):
            U, V = Hermite([t[i], t[i + 1]], j, nt)
            fx = fx + U * x[i + j] + V * Akima(t, x, i+j)
            fy = fy + U * y[i + j] + V * Akima(t, y, i+j)
        plt.plot(fx, fy, color="springgreen", linewidth=1)  # interpolated

    plt.show()


def Intpoints(p, n):
    index = []
    points = []
    step = len(p)/n
    for i in range(n):
        index.append(step*i)
    index.append(index[0])
    index = np.array(index).astype(int)
    for i in index:
        points.append(p[i])
    return points


x = np.loadtxt("X.txt", delimiter=",", unpack=False)
y = np.loadtxt("Y.txt", delimiter=",", unpack=False)
plt.plot(x, y)
plt.show()

n = 100
x = Intpoints(x, n)
y = Intpoints(y, n)
t = np.arange(0, len(x), 1)
Hermite_interpolation(x, y, n, t)
