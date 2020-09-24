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


def iteration_method(intervals, f, alpha, volumeExercise):
    results = []
    # alpha = 1000  # 100# mod for last exercise
    accuracy = 1e-11
    for interval in intervals:
        x = interval[0]
        print("-----FINDING FOR: " + str(x) + "-----")
        iteration = 1
        limit = 20000  # 200# mod for last exercise
        print("v is equal to = " + str(np.round(f(0.32), 2)) + " need v = 0.93")
        # prie kiekvienos saknies reikia parodyti alpha reiksme
        while abs(f(x)) > accuracy and iteration < limit:
            x = x + f(x) / alpha
            iteration += 1
            # plt.plot([x, x, x + f(x) / alpha], [0, f(x), 0])
            print(str(iteration) + " " + str(x) + " " +
                  str(abs(f(x))) + " " + str(alpha))
            # if np.round(f(x), 2) == volumeExercise[1] and volumeExercise[0] == 'y':
            #     break  # mod for last exercise
        # if volumeExercise[0] == 'y':
        #     results.append(np.round(x, 2))
        # else:
            results.append(x)
        alpha *= -1
    return results


def newton_method(intervals, f):
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


def scan_dynamic(intervals, start_step, f):
    accuracy = 1e-11
    results = []
    for interval in intervals:
        step = start_step
        x_from = interval[0]
        x_to = interval[0]
        limit = 200
        iteration = 1
        print("-----FINDING FOR: " + str(x_from) + "------")
        while abs(f(x_from)) > accuracy and iteration < limit:
            iteration += 1
            x_from += step
            if np.sign(f(x_from)) != np.sign(f(x_to)):
                x_from -= step
                step /= 10
                x_to = x_from
            print("iteration: " + str(iteration) + " x/h: " + str(x_from) + " " +
                  str(abs(f(x_from))))
        results.append(x_from)
    return results


# todo: 5th point, 4th point methods require tables with information
acfrom = -4.95744
acto = 4.69721
rgfrom = -14.59574
rgto = 14.59574

accurate_est = [-4.95744, 4.69721]
rough_est = [-14.59574, 14.59574]

# intervals = scan_static(acfrom, acto, 0.5)  # 3
# print("intervals: " + str(intervals))

# points_iteration = iteration_method(
#     intervals, f, 100, ['n', 0])  # v,f,h,df etc
# print("iteration method: " + str(points_iteration))

# points_newton = newton_method(intervals,f)
# print("newton method: " + str(points_newton))

# points_scan_dynamic = scan_dynamic(intervals, 0.1,f)
# print("scan method: " + str(points_scan_dynamic))

# show_graph(np.arange(-5, 3, 0.1), f, (-10, 10),
#            (-4, 4), accurate_est, rough_est, intervals, "teal", points_iteration, "Iteration")  # iteration 4
# show_graph(np.arange(-5, 3, 0.1), f, (-10, 10),
#            (-4, 4), accurate_est, rough_est, intervals, "teal", points_newton, "Newton")  # newton 4
# show_graph(np.arange(-5, 3, 0.1), f, (-10, 10),
#            (-4, 4), accurate_est, rough_est, intervals, "teal", points_scan_dynamic, "Scan dynamic")  # scan_dynamic 4

# show_graph_simple(np.arange(-5, 3, 0.1), g, (-10, 10),
#                   (-4, 4), accurate_est, rough_est, "blue", "g(x)") # g(x) 2
# show_graph_simple(np.arange(-5, 3, 0.1), f, (-10, 10),
#                   (-4, 4), accurate_est, rough_est, "blue", "f(x)")  # f(x) 1

# intervalsLast = [[0.1, 1]]
# points_iteration_volume = iteration_method(
#     intervalsLast, V, 1000, ['y', 0.93])

# print("iteration method: " + str(points_iteration_volume))

# show_graph(np.arange(0, 1, 0.1), V, (-3, 3),
#            (-4, 4), [-2, 2], [-3, 3], intervalsLast, "teal", points_iteration_volume, "Iteration_Volume")  # iteration 4

intervalsLast = [[0.1, 1]]
points_scan_dynamic_volume = scan_dynamic(
    intervalsLast, 0.1, V)

print("iteration method: " + str(points_scan_dynamic_volume))

show_graph(np.arange(0, 1, 0.0000001), V, (-0.25, 3),
           (-4, 4), [-2, 2], [-3, 3], intervalsLast, "teal", points_scan_dynamic_volume, "Scan_Dynamic_Volume")  # iteration 4

# check roots
# roots = fsolve(f, [1.54256, 2.04256])
# print(str(roots) + "*******************")

# roots = fsolve(V, [0.1, 1])
# print(str(roots) + "*******************")
