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


def show_graph(x, func, xlim, ylim, accurate_est, rough_est, intervals, col, points, title):
    plt.plot(x, func(x), col)
    plt.title(title)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.axvline(0, linewidth=0.5, color="black")
    plt.axhline(0, linewidth=0.5, color="black")
    plt.scatter(0, 0, color="black")

    for point in points:  # graph points
        plt.scatter(point, 0, color="green", s=10)
    for a in accurate_est:
        plt.axvline(a, 0, color="red")
    for r in rough_est:
        plt.axvline(r, 0, color="yellow")
    for i in intervals:
        plt.axvline(i[0], 0, linewidth=0.6, color="purple")
        plt.axvline(i[1], 0, linewidth=0.6, color="purple")

    plt.grid()
    plt.show()


def show_graph_simple(x, func, xlim, ylim, accurate_est, rough_est, col, title):
    plt.plot(x, func(x), col)
    plt.title(title)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.axvline(0, linewidth=0.5, color="black")
    plt.axhline(0, linewidth=0.5, color="black")
    plt.scatter(0, 0, color="black")

    for a in accurate_est:
        plt.axvline(a, 0, color="red")
    for r in rough_est:
        plt.axvline(r, 0, color="yellow")

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
            print(str(iteration) + " " + str(x) + " " +
                  str(abs(f(x))) + " " + str(alpha))
        results.append(x)
        alpha *= -1
    return results


def newton_method(intervals):
    results = []
    accuracy = 1e-11
    beta = 0.1  # skirtas konvergavimo taisymui (nebutinas)
    for interval in intervals:
        x = interval[0]
        print("-----FINDING FOR: " + str(x) + "-----")
        iteration = 1
        limit = 500
        while abs(f(x)) > accuracy and iteration < limit:
            x = x - beta * f(x) / df(x)
            iteration += 1
            plt.plot([x, x, x - f(x) / df(x)], [0, f(x), 0])
            print(str(iteration) + " " + str(x) + " " + str(abs(f(x))))
        results.append(x)
    return results


acfrom = -4.95744
acto = 4.69721
rgfrom = -14.59574
rgto = 14.59574

accurate_est = [-4.95744, 4.69721]
rough_est = [-14.59574, 14.59574]

intervals = scan_static(acfrom, acto, 0.5)  # 3
print("intervals: " + str(intervals))

points_iteration = iteration_method(intervals)
print("iteration method: " + str(points_iteration))

points_newton = newton_method(intervals)
print("iteration method: " + str(points_newton))

# show_graph(np.arange(-5, 3, 0.1), f, (-10, 10),
#            (-4, 4), acfrom, acto, rgfrom, rgto, intervals, "teal", points_iteration, "Iteration") # iteration 4
show_graph(np.arange(-5, 3, 0.1), f, (-10, 10),
           (-4, 4), accurate_est, rough_est, intervals, "teal", points_newton, "Newton")  # newton 4
# show_graph_simple(np.arange(-5, 3, 0.1), g, (-10, 10),
#                   (-4, 4), accurate_est, rough_est, "blue", "g(x)") # g(x) 2
# show_graph_simple(np.arange(-5, 3, 0.1), f, (-10, 10),
#                   (-4, 4), accurate_est, rough_est, "blue", "f(x)")  # f(x) 1

# check roots
# roots = fsolve(f, [1.54256, 2.04256])
# print(str(roots) + "*******************")
