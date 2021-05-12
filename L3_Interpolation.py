import numpy as np
import matplotlib.pyplot as plt
import os
import time
import scipy.integrate

plt.style.use('bmh')
os.system("cls")


def f(x):
    return (np.cos(2 * x) * np.sin(3 * x) + 1.5) - np.cos(x / 5)


def chebyshev_base_formula(i, x):
    return np.cos(i * np.arccos(x))


def chebyshev_interp_interval(nodes, min, max):
    return (2 * nodes) / (max - min) - (max + min) / (max - min)


def chebyshev_distrubution(min, max, N, i):
    return ((max - min) / 2) * np.cos((np.pi * (2 * i + 1)) / (2 * N)) + ((max + min) / 2)


def interpolated_f_print(st):
    for i in range(len(st)):
        if i == 0:
            print(str(st[i]) + "+,", end="")
        elif i == len(st)-1:
            print(str(st[i]) + "*T_" + str(i) + "(x)", end="")
        else:
            print(str(st[i]) + "*T_" + str(i) + "(x)" + "+", end="")
# (0.5+0.6*T_1(x)...T_n(X)) form


def chebyshev_interpolation_old(min, max, N, ch):
    i = np.arange(N)  # node count split for iteration

    if ch == 'ch':
        X = np.vstack(chebyshev_distrubution(min, max, N, i))
    else:
        X = np.vstack(np.linspace(min, max, N))

    Y = f(X)  # new y that matches x interval
    X_cheb = chebyshev_interp_interval(X, min, max)  # -1to1
    T = chebyshev_base_formula(i, X_cheb)  # base function calc
    a_coef = np.linalg.solve(T, Y)  # coefficient calc

    X = np.vstack(np.linspace(min, max, 100))  # main X
    Y = f(X)  # main Y
    X_cheb = chebyshev_interp_interval(X, min, max)  # interpolated x
    T = chebyshev_base_formula(i, X_cheb)
    Y_cheb = T @ a_coef  # interpolated y

    plt.plot(X, Y_cheb, color="blue", linewidth=1)  # interpolated
    plt.plot(X, Y, color="red", linewidth=1)
    plt.plot(X, Y-Y_cheb, color="green", linewidth=1)
    plt.legend(['Interpolated f(x)', 'f(x)', 'error'])
    interpolated_f_print(a_coef)
    plt.show()


def base_m(x, N, arange):
    base = np.ones((arange, N))
    base[:, 1] = x[:arange]
    for j in range(2, N):
        base[:, j] = 2 * x * base[:, j - 1] - base[:, j - 2]
    return base


def chebyshev_interpolation(min, max, N, ch, arange):

    if ch == 'ch':
        X = chebyshev_distrubution(min, max, N, np.arange(N))
    else:
        X = np.linspace(min, max, N)

    base_matrix = base_m(X, N, N)
    Y = f(X)
    a_coef = np.linalg.solve(base_matrix, Y)
    X_cheb = np.linspace(min, max, arange)
    new_base_matrix = base_m(X_cheb, N, arange)
    Y_cheb = np.zeros(arange)
    Y_cheb = new_base_matrix @ a_coef

    plt.plot(X_cheb, Y_cheb, color="blue", linewidth=1)  # interpolated
    plt.plot(X_cheb, f(X_cheb), color="red", linewidth=1)  # not interpolated
    plt.plot(X_cheb, f(X_cheb)-Y_cheb, color="green", linewidth=1)
    plt.legend(['Interpolated f(x)', 'f(x)', 'error'])
    interpolated_f_print(a_coef)
    plt.show()


chebyshev_interpolation(-2, 3, 20, 'ch', 1000)
# chebyshev_interpolation_old(-2, 3, 4, '')
