import numpy as np
import matplotlib.pyplot as plt
import os
os.system("cls")
# e = np.finfo(float).eps
e = 2.71828


def f(x):
    return 0.47*x**4 + 1.86*x**3 - 1.01*x**2 - 6.39*x-1.85


def df(x):  # isvestine
    return 1.88*x**3 + 5.58*x**2 - 2.02*x - 6.39

# transcendentinė funkcija


def g(x):
    return e**x + e**-x - 100*np.sin(x)**2


def show_graph(x, func, xlim, ylim, xline1, xline2, xline3, xline4):
    plt.plot(x, func(x))
    plt.xlim(xlim)
    plt.ylim(ylim)
    if(xline1 != 0 and xline2 != 0 and xline3 != 0 and xline4 != 0):
        plt.axvline(xline1, 0, color="red")  # tikslus
        plt.axvline(xline2, 0, color="red")  # tikslus
        plt.axvline(xline3, 0, color="yellow")  # grubus
        plt.axvline(xline4, 0, color="yellow")  # grubus
    plt.grid()
    plt.show()


show_graph(np.arange(-1, 6, 1), g, (-10, 10), (-4, 4), 0, 0, 0, 0)
show_graph(np.arange(-5, 3, 0.1), f, (-10, 10),
           (-4, 4), -4.95744, 4.69721, -14.59574, 14.59574)
# gx = np.arange(-1, 6, 1)
# plt.plot(gx, g(gx))
# plt.grid()
# plt.show()
# print(g(1))
# print(e)
# # transcendentinė funkcija

# x = np.arange(-5, 3, 0.1)
# plt.plot(x, f(x))
# # plt.ylim((-2, 2))
# # plt.xlim((-10, 10))

# plt.axvline(-4.95744, 0, color="red")  # tikslus
# plt.axvline(4.68721, 0, color="red")  # tikslus
# plt.axvline(-14.59574, 0, color="yellow")  # grubus
# plt.axvline(14.59574, 0, color="yellow")  # grubus
# plt.grid()
# plt.show()
# print(f(1))
