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


def dg(x):
    return np.e**x - np.e**-x - 100*np.sin(2*x)


def V(h):
    r = 3
    v = 0.93
    return (np.pi*h**2*(3*r-h))/3 - v


def show_graph(x, func, xlim, ylim, accurate_est, rough_est, intervals, col, points, title):
    plt.plot(x, func(x), col)
    plt.title(title)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.axvline(0, linewidth=0.5, color="black")
    plt.axhline(0, linewidth=0.5, color="black")
    plt.scatter(0, 0, color="black")

    for point in points:
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


def scan_static(accurate_est, step, f):
    intervals = []
    first = accurate_est[0]
    last = accurate_est[1]
    while first < accurate_est[1]:
        last = first + step
        if np.sign(f(first)) != np.sign(f(last)):
            intervals.append([first, last])
        first = last
    return intervals


def iteration_method(intervals, f, alpha):
    results = []
    information = []
    accuracy = 1e-11
    for interval in intervals:
        x = interval[0]
        iteration = 1
        limit = 2000
        while abs(f(x)) > accuracy and iteration < limit:
            x = x + f(x) / alpha
            iteration += 1
        results.append(x)
        information.append(
            ["iterations: " + str(iteration), "from interval: " + str(interval[0]),  "to interval: " + str(interval[1]), "alpha: " + str(alpha), "accuracy: " + str(accuracy)])
        alpha *= -1
    return results, information


def newton_method(intervals, f, df):
    results = []
    information = []
    accuracy = 1e-11
    beta = 1
    for interval in intervals:
        x = interval[0]
        iteration = 1
        limit = 2000
        while abs(f(x)) > accuracy and iteration < limit:
            x = x - beta * f(x) / df(x)
            iteration += 1
            plt.plot([x, x, x - f(x) / df(x)], [0, f(x), 0])
        results.append(x)
        information.append(
            ["iterations: " + str(iteration), "from interval: " + str(interval[0]),  "to interval: " + str(interval[1]), "accuracy: " + str(accuracy), "beta: " + str(beta)])
    return results, information


def dynamic_scan(intervals, start_step, f):
    accuracy = 1e-11
    results = []
    information = []
    for interval in intervals:
        step = start_step
        x_from = interval[0]
        x_to = interval[0]
        limit = 2000
        iteration = 1
        while abs(f(x_from)) > accuracy and iteration < limit:
            iteration += 1
            x_from += step
            if np.sign(f(x_from)) != np.sign(f(x_to)):
                x_from -= step
                step /= 10
                x_to = x_from
        results.append(x_from)
        information.append(
            ["iterations: " + str(iteration), "from interval: " + str(interval[0]),  "to interval: " + str(interval[1]), "accuracy: " + str(accuracy)])
    return results, information


def info_print(information, intervals, title):
    os.system("cls")
    print(title + "\n")
    print("INTERVALS: " + str(intervals) + "\n")
    print("ROOTS: " + str(information[0]) + "\n")
    it = 0
    for info in information[1]:
        print("---------FOUND ROOT: " +
              str(information[0][it])+"--------------")
        for i in info:
            print(str(i))
        it += 1
    print("-----------------------------------------------------")


accurate_est = [-4.95744, 4.68724]
rough_est = [-14.59574, 14.59574]
accurate_est_g = [-1, 6]

print("1 - - - f(x) Iteration method")
print("2 - - - f(x) Newton method")
print("3 - - - f(x) Dynamic scan method")
print("4 - - - VOLUME exercise method")
print("5 - - - show f(x)")
print("6 - - - show g(x)")
print("7 - - - g(x) Iteration method")
print("8 - - - g(x) Newton method")
print("9 - - - g(x) Dynamic scan method")

option = input()

if option == '1':
    title = "f(x) Iteration method"
    intervals = scan_static(accurate_est, 0.5, f)
    points_iteration = iteration_method(intervals, f, 100)
    info_print(points_iteration, intervals, title)
    show_graph(np.arange(-5, 3, 0.1), f, (-10, 10),
               (-4, 4), accurate_est, rough_est, intervals, "teal", points_iteration[0], title)

elif option == '2':
    title = "f(x) Newton method"
    intervals = scan_static(accurate_est, 0.5, f)
    points_newton = newton_method(intervals, f, df)
    info_print(points_newton, intervals, title)
    show_graph(np.arange(-5, 3, 0.1), f, (-10, 10),
               (-4, 4), accurate_est, rough_est, intervals, "teal", points_newton[0], title)

elif option == '3':
    title = "f(x) Scan dynamic method"
    intervals = scan_static(accurate_est, 0.5, f)
    points_dynamic_scan = dynamic_scan(intervals, 0.1, f)
    info_print(points_dynamic_scan, intervals, title)
    show_graph(np.arange(-5, 3, 0.1), f, (-10, 10),
               (-4, 4), accurate_est, rough_est, intervals, "teal", points_dynamic_scan[0], title)

elif option == '4':
    title = "Scan dynamic volume"
    intervals = [[0.1, 1]]
    points_dynamic_scan_volume = dynamic_scan(intervals, 0.1, V)
    info_print(points_dynamic_scan_volume, intervals, title)
    show_graph(np.arange(0, 1, 0.0000001), V, (-0.25, 3),
               (-4, 4), [-2, 2], [-3, 3], intervals, "teal", points_dynamic_scan_volume[0], title)

elif option == '5':
    print("f(x)")
    show_graph_simple(np.arange(-5, 3, 0.1), f, (-10, 10), (-4, 4),
                      accurate_est, rough_est, "blue", "f(x)")
elif option == '6':
    print("g(x)")
    show_graph_simple(np.arange(-1, 6, 0.00001), g, (-1, 6),
                      (-4, 4), accurate_est_g, rough_est, "blue", "g(x)")

elif option == '7':
    title = "g(x) Iteration method"
    intervals = scan_static(accurate_est_g, 0.1, g)  # 3
    points_iteration = iteration_method(intervals, g, -100)
    info_print(points_iteration, intervals, title)
    show_graph(np.arange(-1, 6, 0.00001), g, (-1, 6),
               (-4, 4), accurate_est_g, [0, 0], intervals, "teal", points_iteration[0], title)

elif option == '8':
    title = "g(x) Newton method"
    intervals = scan_static(accurate_est_g, 0.1, g)
    points_newton = newton_method(intervals, g, dg)
    info_print(points_newton, intervals, title)
    show_graph(np.arange(-1, 6, 0.00001), g, (-1, 6),
               (-4, 4), accurate_est_g, [0, 0], intervals, "teal", points_newton[0], title)

elif option == '9':
    title = "g(x) Dynamic scan method"
    intervals = scan_static(accurate_est_g, 0.5, g)
    points_dynamic_scan_volume = dynamic_scan(intervals, 0.1, g)
    info_print(points_dynamic_scan_volume, intervals, title)
    show_graph(np.arange(-1, 6, 0.00001), g, (-1, 6),
               (-4, 4), accurate_est_g, [0, 0], intervals, "teal", points_dynamic_scan_volume[0], title)
