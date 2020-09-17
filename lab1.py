import numpy as np
import matplotlib.pyplot as plt
import os

os.system("cls")


def f(x):
    return 0.47*x**4 + 1.86*x**3 - 1.01*x**2 - 6.39*x-1.85


def df(x):
    return 1.88*x**3 + 5.58*x**2 - 2.02*x - 6.39


def g(x):
    return np.e**x + np.e**-x - 100*np.sin(x)**2


def show_graph(x, func, xlim, ylim, xline1, xline2, xline3, xline4, intervals):
    plt.plot(x, func(x))
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.axvline(0, linewidth=0.5, color="black")
    plt.axhline(0, linewidth=0.5, color="black")
    plt.scatter(0, 0, color="black")
    plt.scatter(-3.584, 0, color="green")  # f(x) grafiko taskai
    plt.scatter(-1.903, 0, color="green")
    plt.scatter(-0.313, 0, color="green")
    plt.scatter(1.843, 0, color="green")

    if(xline1 != -999):
        plt.axvline(xline1, 0, color="red")  # tikslus
        plt.axvline(xline2, 0, color="red")  # tikslus
        plt.axvline(xline3, 0, color="yellow")  # grubus
        plt.axvline(xline4, 0, color="yellow")  # grubus

    # intervals
    intervals.sort()  # remove
    for i in intervals:
        plt.axvline(i, 0, linewidth=0.5, color="purple")
        print(i)

    plt.grid()
    plt.show()


def scan_method(acfrom, acto):  # ??
    accur = 1
    rn = np.arange(-4.95744, 4.69721, accur)
    vals = f(rn).tolist()
    intervals = list()
    for item in vals:
        if item > acfrom and item < acto:
            intervals.append(item)
    return intervals

# show_graph(np.arange(-1, 6, 0.1), g, (-1, 6),
#            (-4, 4), -999, 0, 0, 0)  # g(x)
# show_graph(np.arange(-5, 3, 0.1), f, (-10, 10),
#            (-4, 4), -4.95744, 4.69721, -14.59574, 14.59574)  # f(x)


acfrom = -4.95744
acto = 4.69721
intervals = scan_method(acfrom, acto)


show_graph(np.arange(-5, 3, 0.1), f, (-10, 10),
           (-4, 4), -4.95744, 4.69721, -14.59574, 14.59574, intervals)  # f(x)
