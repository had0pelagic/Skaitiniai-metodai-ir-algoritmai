import numpy as np
import matplotlib.pyplot as plt
import os
import time
import scipy.integrate

plt.style.use('bmh')
os.system("cls")


def interpolated_f_print(st):
    for i in range(len(st)):
        if i == 0:
            print(str(st[i]) + "+,", end="")
        elif i == len(st)-1:
            print(str(st[i]) + "*T_" + str(i) + "(x)", end="")
        else:
            print(str(st[i]) + "*T_" + str(i) + "(x)" + "+", end="")


def Base_m(x, N, arange):
    base = np.ones((arange, N))
    base[:, 1] = x[:arange]
    for j in range(2, N):
        base[:, j] = 2 * x * base[:, j - 1] - base[:, j - 2]
    return base


def Chebyshev_interpolation(x, y, N, arange):
    base_matrix = Base_m(x, N, N)
    a_coef = np.linalg.solve(base_matrix, y)

    X_cheb = np.linspace(0, 11, arange)
    new_base_matrix = Base_m(X_cheb, N, arange)
    Y_cheb = np.zeros(arange)
    Y_cheb = new_base_matrix @ a_coef

    interpolated_f_print(a_coef)
    plt.title("Cheb")
    plt.xlabel(
        'Sep   Oct   Nov   Dec   Jan   Feb   Mar   Apr   May   Jun   Jul   Aug')
    plt.ylabel('Temperatures')
    plt.xticks(np.arange(0, len(y)))
    plt.scatter(x, y, s=10, c="purple")
    plt.plot(X_cheb, Y_cheb, color="blue", linewidth=1)  # base
    plt.plot(x, y, color="red", linewidth=1)  # normal
    plt.legend(['Base', 'Normal'])
    plt.show()


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


def Hermite_interpolation(x, y, nv):
    plt.plot(x, y, color="red", linewidth=1)  # normal
    for i in range(0, len(x) - 1):
        X = np.linspace(x[i], x[i + 1], nv)
        f = 0
        for j in range(0, 2):  # 2 times because of defect
            U, V = Hermite([x[i], x[i + 1]], j, X)
            # Hermite interpolation expression
            f = f + U * y[i + j] + V * Akima(x, y, i+j)
        plt.plot(X, f, color="blue", linewidth=1)  # interpolated

    plt.title("Hermite")
    plt.xlabel(
        'Sep   Oct   Nov   Dec   Jan   Feb   Mar   Apr   May   Jun   Jul   Aug')
    plt.ylabel('Temperatures')
    plt.xticks(np.arange(0, len(y)))
    plt.scatter(x, y, s=10, c="purple")
    plt.legend(['Normal', 'Interpolated'])
    plt.show()


y = [-22.503, -24.093, -8.1384, 3.77994, 9.4613, 16.4551,
     19.5725, 17.5124, 10.4751, 2.8363, -7.7963, -19.833]
x = np.arange(0, len(y))
n = 12
nv = 1000
# Chebyshev_interpolation(x, y, n, nv)
Hermite_interpolation(x, y, nv)
