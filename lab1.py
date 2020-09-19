import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.optimize import fsolve

os.system("cls")


def f(x):
    return 0.47*x**4 + 1.86*x**3 - 1.01*x**2 - 6.39*x-1.85


def df(x):
    return 1.88*x**3 + 5.58*x**2 - 2.02*x - 6.39


def g(x):
    return np.e**x + np.e**-x - 100*np.sin(x)**2


def show_graph(x, func, xlim, ylim, xline1, xline2, xline3, xline4, intervals, col, points):
    plt.plot(x, func(x), col)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.axvline(0, linewidth=0.5, color="black")
    plt.axhline(0, linewidth=0.5, color="black")
    plt.scatter(0, 0, color="black")

    for point in points:  # graph points
        plt.scatter(point, 0, color="green", s=10)

    if(xline1 != -999):
        plt.axvline(xline1, 0, color="red")  # tikslus
        plt.axvline(xline2, 0, color="red")  # tikslus
        plt.axvline(xline3, 0, color="yellow")  # grubus
        plt.axvline(xline4, 0, color="yellow")  # grubus

    # intervals
    intervals.sort()  # remove
    for i in intervals:
        plt.axvline(i[0], 0, linewidth=0.6, color="purple")
        plt.axvline(i[1], 0, linewidth=0.6, color="purple")

    plt.grid()
    plt.show()


def scan_static(acfrom, acto, step):
    intervals = []
    first = acfrom
    last = acto
    while first < acto:
        last = first + step
        if np.sign(f(first)) != np.sign(f(last)):
            # print(str(f(first)) + " " + str(f(last)) + "////////////////////")
            # print(str(first) + " " + str(last) + "--------------")
            intervals.append([first, last])
        first = last
    return intervals


def iteration_method(intervals):
    results = []
    alpha = 100
    accuracy = 1e-11
    for interval in intervals:
        x = interval[0]
        print("-----FINDING FOR: " + str(x) + "-----")
        iteration = 1
        limit = 200
        while abs(f(x)) > accuracy and iteration < limit:
            x = x + f(x) / alpha
            iteration += 1
            plt.plot([x, x, x + f(x) / alpha], [0, f(x), 0])
            # print(str(iteration) + " " + str(x) + " " +
            #       str(abs(f(x))) + " " + str(alpha))
        results.append(x)
        alpha *= -1
    return results


# show_graph(np.arange(-1, 6, 0.1), g, (-1, 6),
#            (-4, 4), -999, 0, 0, 0)  # g(x) 2uzd
# show_graph(np.arange(-5, 3, 0.1), f, (-10, 10),
#            (-4, 4), -4.95744, 4.69721, -14.59574, 14.59574)  # f(x) 1uzd
acfrom = -4.95744
acto = 4.69721
intervals = scan_static(acfrom, acto, 0.5)
print("intervals: " + str(intervals))
points_iteration = iteration_method(intervals)
print("iteration method: " + str(points_iteration))
show_graph(np.arange(-5, 3, 0.1), f, (-10, 10),
           (-4, 4), -4.95744, 4.69721, -14.59574, 14.59574, intervals, "blue", points_iteration)  # f(x)
# show_graph(np.arange(-5, 3, 0.1), df, (-10, 10),
#            (-4, 4), -4.95744, 4.69721, -14.59574, 14.59574, intervals, "teal")  # f(x)

# check roots
# roots = fsolve(f, [1.54256, 2.04256])
# print(str(roots) + "*******************")
