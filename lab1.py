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


def scan_static(accurate_est, step):
    intervals = []
    first = accurate_est[0]
    last = accurate_est[1]
    while first < accurate_est[1]:
        last = first + step
        if np.sign(f(first)) != np.sign(f(last)):
            # print(str(f(first)) + " " + str(f(last)) + "////////////////////")
            # print(str(first) + " " + str(last) + "--------------")
            intervals.append([first, last])
        first = last
    return intervals


def iteration_method(intervals, f, alpha):
    results = []
    information = []
    accuracy = 1e-11
    for interval in intervals:
        x = interval[0]
        # print("-----FINDING FOR: " + str(x) + "-----")
        iteration = 1
        limit = 200
        while abs(f(x)) > accuracy and iteration < limit:
            x = x + f(x) / alpha
            iteration += 1
            # plt.plot([x, x, x + f(x) / alpha], [0, f(x), 0])
            # print(str(iteration) + " " + str(x) + " " +
            #       str(abs(f(x))) + " " + str(alpha))
        results.append(x)
        information.append(
            ["iterations: " + str(iteration), "from interval: " + str(interval[0]),  "to interval: " + str(interval[1]), "alpha: " + str(alpha), "accuracy: " + str(accuracy)])
        alpha *= -1
    return results, information


def newton_method(intervals, f):
    results = []
    information = []
    accuracy = 1e-11
    beta = 0.1  # skirtas konvergavimo taisymui (nebutinas)
    for interval in intervals:
        x = interval[0]
        # print("-----FINDING FOR: " + str(x) + "-----")
        iteration = 1
        limit = 500
        while abs(f(x)) > accuracy and iteration < limit:
            x = x - beta * f(x) / df(x)
            iteration += 1
            plt.plot([x, x, x - f(x) / df(x)], [0, f(x), 0])
            # print(str(iteration) + " " + str(x) + " " + str(abs(f(x))))
        results.append(x)
        information.append(
            ["iterations: " + str(iteration), "from interval: " + str(interval[0]),  "to interval: " + str(interval[1]), "accuracy: " + str(accuracy), "beta: " + str(beta)])
    return results, information


def scan_dynamic(intervals, start_step, f):
    accuracy = 1e-11
    results = []
    information = []
    for interval in intervals:
        step = start_step
        x_from = interval[0]
        x_to = interval[0]
        limit = 200
        iteration = 1
        # print("-----FINDING FOR: " + str(x_from) + "------")
        while abs(f(x_from)) > accuracy and iteration < limit:
            iteration += 1
            x_from += step
            if np.sign(f(x_from)) != np.sign(f(x_to)):
                x_from -= step
                step /= 10
                x_to = x_from
            # print("iteration: " + str(iteration) + " x/h: " + str(x_from) + " " +
            #       str(abs(f(x_from))))
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


accurate_est = [-4.95744, 4.69721]
rough_est = [-14.59574, 14.59574]

print("1 - - - iteration method")
print("2 - - - newton method")
print("3 - - - dynamic scan method")
print("4 - - - volume exercise method")
print("5 - - - show f(x) interval")
print("6 - - - show g(x)")

option = input()

if option == '1':
    title = "Iteration method"
    intervals = scan_static(accurate_est, 0.5)  # 3

    points_iteration = iteration_method(intervals, f, 100)

    info_print(points_iteration, intervals, title)

    show_graph(np.arange(-5, 3, 0.1), f, (-10, 10),
               (-4, 4), accurate_est, rough_est, intervals, "teal", points_iteration[0], title)  # iteration 4

elif option == '2':
    title = "Newton method"
    intervals = scan_static(accurate_est, 0.5)  # 3

    points_newton = newton_method(intervals, f)

    info_print(points_newton, intervals, title)

    show_graph(np.arange(-5, 3, 0.1), f, (-10, 10),
               (-4, 4), accurate_est, rough_est, intervals, "teal", points_newton[0], title)  # newton 4

elif option == '3':
    title = "Scan dynamic method"
    intervals = scan_static(accurate_est, 0.5)  # 3

    points_scan_dynamic = scan_dynamic(intervals, 0.1, f)

    info_print(points_scan_dynamic, intervals, title)

    show_graph(np.arange(-5, 3, 0.1), f, (-10, 10),
               (-4, 4), accurate_est, rough_est, intervals, "teal", points_scan_dynamic[0], title)  # scan_dynamic 4

elif option == '4':
    title = "Scan dynamic volume"
    intervals = [[0.1, 1]]

    points_scan_dynamic_volume = scan_dynamic(intervals, 0.1, V)

    info_print(points_scan_dynamic_volume, intervals, title)

    show_graph(np.arange(0, 1, 0.0000001), V, (-0.25, 3),
               (-4, 4), [-2, 2], [-3, 3], intervals, "teal", points_scan_dynamic_volume[0], title)  # iteration 4

elif option == '5':
    print("f(x)")
    show_graph_simple(np.arange(-5, 3, 0.1), f, (-10, 10), (-4, 4),
                      accurate_est, rough_est, "blue", "f(x)")  # f(x) 1
elif option == '6':
    print("g(x)")
    show_graph_simple(np.arange(-5, 3, 0.1), g, (-10, 10),
                      (-4, 4), accurate_est, rough_est, "blue", "g(x)")  # g(x) 2
elif option == '7':
    title = "g(x) with roots Iteration method "  # need all methods
    intervals = [[0.1, 1]]

    points_scan_dynamic_volume = scan_dynamic(intervals, 0.1, V)

    info_print(points_scan_dynamic_volume, intervals, title)

    show_graph(np.arange(0, 1, 0.0000001), V, (-0.25, 3),
               (-4, 4), [-2, 2], [-3, 3], intervals, "teal", points_scan_dynamic_volume[0], title)  # iteration 4
