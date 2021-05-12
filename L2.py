import numpy as np
import matplotlib.pyplot as plt
import os
import time
os.system("cls")

# 2    1    1    1    6
# 1    3    1   -3   -4
# 1    1    5    1    4
# 2    3   -3   -2    0

A = np.matrix([[2, 1,  1,  1],
               [1, 3, 1,  -3],
               [1,  1, 5,  1],
               [2,  3,  -3, -2]]).astype(np.float)  # equations
b = (np.matrix([6, -4, 4, 0])).transpose().astype(np.float)  # wanted results
n = (np.shape(A))[0]  # equation count
nb = (np.shape(b))[1]  # wanted result count
Aextended = np.hstack((A, b))  # equation combine


def Res_print(matrix, title, iteration):
    print(str(iteration) + "=======================================")
    print('-----' + str(title) + '----')
    print(matrix)
    print('---------')


def QR(A, b, n, nb, Aextended):
    Q = np.identity(n)
    for i in range(0, n-1):
        z = Aextended[i:n, i]
# extract vector from matrix
        Res_print(z, 'z', i)
        zref = np.zeros(np.shape(z))
        zref[0] = np.linalg.norm(z)
# calc vector reflection
        Res_print(zref, 'zref', i)
        omega = z-zref
        omega = omega/np.linalg.norm(omega)
# find plane normal
        Res_print(omega, 'omega', i)
        Qi = np.eye(n-i)-2*omega*np.transpose(omega)
# calc vector reflection matrix
        Res_print(Qi, 'Qi', i)
        Aextended[i:n] = Qi.dot(Aextended[i:n])
# calc main matrix * reflection matrix (column reflection creation inside)
        Res_print(Aextended, 'A', i)
        Q = Q.dot(np.vstack(
            (
                np.hstack((np.identity(i), np.zeros(shape=(i, n-i)))),
                np.hstack((np.zeros(shape=(n-i, i)), Qi))
            )
        ))
# calc diagonal 1's matrix * matrix if i = 1 -> [[1],[0 0 0]/[0,0,0],[Qi]]
        Res_print(Q, 'Q', i)
# result calc res=R (triangular matrix) * unknown
# res -> triangular matrix 0.2x4 =... 0.111x4 -4= ... ant etc
    res = Q.transpose().dot(b)
    x = np.zeros(shape=(n, nb))
    for i in range(n-1, -1, -1):
        x[i] = (res[i]-Aextended[i, i+1:n]*x[i+1:n])/Aextended[i, i]

    Res_print(x, 'answer', -1)
    sum = 0
    for i in range(0, n):
        for g in range(0, n):
            sum += A[i, g] * x[g]
        print(sum)
        sum = 0
# ============================================================================================================================================


def LF(x, y, z):
    if z == 1:
        res = (x/8)**8 + (y/8)**8 - 1
    if z == 2:
        res = (x**2) * (y**2) - 16
    return res


def nonlinear_graphical():
    X = np.arange(-10, 10, 0.25)
    Y = np.arange(-10, 10, 0.25)
    XX, YY = np.meshgrid(X, Y)
    Z1 = LF(XX, YY, 1)
    Z2 = LF(XX, YY, 2)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    sf1 = ax.plot_surface(XX, YY, Z1, color="red", alpha=0.2)
    sfz1 = ax.plot_surface(XX, YY, np.zeros(np.shape(Z1)), alpha=0.2)
    zline1 = ax.contour(X, Y, Z1, levels=0, colors="red")
    plt.show()
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    sf2 = ax.plot_surface(XX, YY, Z2, color="blue", alpha=0.2)
    sfz2 = ax.plot_surface(XX, YY, np.zeros(np.shape(Z2)), alpha=0.2)
    zline2 = ax.contour(X, Y, Z2, levels=0, colors="blue")
    plt.show()
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    co2 = ax.contour(X, Y, Z1, levels=0, colors="red")
    co2 = ax.contour(X, Y, Z2, levels=0, colors="blue")
    plt.show()
# ============================================================================================================================================


def nonlinear_func_two(x):
    return np.array([[(x[0]/8)**8 + (x[1]/8)**8 - 1],
                     [(x[0]**2) * (x[1]**2) - 16]])


def target_two(x):
    return 0.5*np.sum(nonlinear_func_two(x)*nonlinear_func_two(x))


def gradient_two(x):
    h = 1e-4
    return np.array([(target_two([x[0] + h, x[1]]) - target_two(x)) / h, (target_two([x[0], x[1] + h]) - target_two(x)) / h])


def gradient_descent_two():
    step_limit = 1e-5
    step = 0.1
    x = np.array([-4, 8])
    f_old = target_two(x)
    grad = gradient_two(x)

    for i in range(600000):
        x = x - step * (grad/np.linalg.norm(grad))
        f_new = target_two(x)

        if f_new > f_old:
            x = x + step * (grad/np.linalg.norm(grad))
            step = step/1.002
            grad = gradient_two(x)

        else:
            f_old = f_new

        print(f'x: {x} || old: {f_old} || i {i}')

        if step < step_limit:
            break
    print(x)
    print(nonlinear_func_two(x))
# ============================================================================================================================================


def nonlinear_func_four(x):
    return np.array([[3*x[0] + 4*x[1] - 3*x[2] + 4*x[3] + 25],
                     [5*x[2] + 4*x[1]*x[2] + 55],
                     [5*x[3]**3 - 2*x[3]**2 + x[1]*x[2] - 97],
                     [2*x[0] - 12*x[1] + 4*x[2] + 4*x[3] - 76],
                     ])


def target_four(x):
    return 0.5*np.sum(nonlinear_func_four(x)*nonlinear_func_four(x))


def gradient_four(x):
    h = 1e-13
    return np.array([(target_four([x[0] + h, x[1], x[2], x[3]]) - target_four(x)) / h,
                     (target_four([x[0], x[1] + h, x[2], x[3]]) -
                      target_four(x)) / h,
                     (target_four([x[0], x[1], x[2] + h, x[3]]) -
                      target_four(x)) / h,
                     (target_four([x[0], x[1], x[2], x[3] + h]) - target_four(x)) / h])


def gradient_descent_four():
    step_limit = 1e-5
    step = 0.1
    x = np.array([-0.5, -0.5, 1, 1])  # -2, -4, 5, 3
    f_old = target_four(x)
    grad = gradient_four(x)
    for i in range(600000):
        x = x - step * (grad/np.linalg.norm(grad))
        f_new = target_four(x)

        if f_new > f_old:
            x = x + step * (grad/np.linalg.norm(grad))
            step = step/1.002
            grad = gradient_four(x)

        else:
            f_old = f_new

        # print(f'x: {x[3]} || old: {f_old} || i {i}')
        print(f'x: {x} || i {i} || old : {f_old} ')

        if step < step_limit:
            break
    print(x)
    print(nonlinear_func_four(x))

# ============================================================================================================================================


def points(n):
    points = [(0, 0)]
    for i in range(n):
        x = np.random.randint(-10, 10)
        y = np.random.randint(-10, 10)
        points.append((x, y))
    print(points)

    return np.array(points)


def vector_length_sum(points):
    ret = 0
    count = len(points)
    for f in range(count):
        for s in range(f+1, count):
            f1 = points[f][0]  # first
            s1 = points[s][0]
            f2 = points[f][1]
            s2 = points[s][1]
            fr = s1 - f1
            to = s2 - f2
            ret += length(fr, to)

    return ret


def length(fr, to):
    return np.sqrt(fr**2 + to**2)


def price(points, a):  # l - road len, alpha > 0
    l = vector_length_sum(points)
    return (l-a)**2


def grad_optimize(points, a):
    h = 1e-3
    count = len(points)
    gradient = []
    for i in range(1, count):
        insert_from = points[1:i]
        insert_to = points[i+1:]
        insert_changed_x = [points[i][0] + h, points[i][1]]
        array = np.vstack(
            (insert_from, insert_changed_x, insert_to))

        x = (price(array, a) - price(points, a))/h

        insert_changed_y = [points[i][0] + h, points[i][1]]
        array = np.vstack(
            (insert_from, insert_changed_y, insert_to))

        y = (price(array, a) - price(points, a))/h

        gradient.append((x, y))
    return gradient


def optimize(points, a):
    step = 0.01
    f_old = price(points, a)
    grad = grad_optimize(points, a) / np.linalg.norm(grad_optimize(points, a))
    grad = np.array(grad)
    for i in range(15):
        points[1:] = points[1:] - step * (grad/np.linalg.norm(grad))
        f_new = price(points, a)
        print(f'new : {f_new}   old : {f_old}')
        if f_new > f_old:
            points[1:] = points[1:] + step * (grad/np.linalg.norm(grad))
            step = step/1.02
            grad = grad / np.linalg.norm(grad)
        else:
            f_old = f_new

    return points


def visual(points):
    plt.axis((-10, 10, -10, 10))
    plt.grid(color='r', linewidth=0.1)
    print(points[0, 0])
    plt.axvline(0, linewidth=0.5, color="black")
    plt.axhline(0, linewidth=0.5, color="black")
    print(points)
    for point in points:
        plt.scatter(point[0], point[1])
        plt.text(point[0], point[1], f'({point[0]}, {point[1]})')
    plt.show()
# ============================================================================================================================================


choice = input()

if(choice == str(1)):
    QR(A, b, n, nb, Aextended)

if(choice == str(2)):
    nonlinear_graphical()

if(choice == str(3)):
    gradient_descent_two()

if(choice == str(4)):
    gradient_descent_four()

if(choice == str(5)):
    a = 2
    points = points(5)
    price(points, a)
    visual(points)
    print(f'first price: {price(points, a)}')
    newpoints = optimize(points, a)
    visual(points)
    print(f'last price: {price(points, a)}')
