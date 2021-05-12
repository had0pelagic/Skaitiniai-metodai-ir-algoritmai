import numpy as np
import matplotlib.pyplot as plt
import os
import time
import scipy.integrate

plt.style.use('bmh')
os.system("cls")


def Base(x, m):
    g = np.zeros((len(x), m))
    for i in range(m):
        g[:, i] = x**i
    return g


def F(x, c):
    y = np.zeros(len(x))
    for g in range(len(x)):
        rs = 0
        for i in range(len(c)):
            rs += c[i] * x[g]**i
        y[g] = rs
    return y


def Func_print(c):
    for i in range(len(c)):
        print(str(c[i]) + '*x^'+str(i)+'+')


y = [-22.503, -24.093, -8.1384, 3.77994, 9.4613, 16.4551,
     19.5725, 17.5124, 10.4751, 2.8363, -7.7963, -19.833]
x = np.arange(0, len(y))
nv = 1000
deg = 5
deg += 1

G = Base(x, deg)
c = np.linalg.solve(np.transpose(G) @ G, np.transpose(G) @ y)
Func_print(c)
x_o = np.linspace(0, len(y)-1, nv)
y_o = F(x_o, c)

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(x, y, color="red", linewidth=1)
ax.plot(x_o, y_o, color="gold")
ax.scatter(x, y)
plt.show()
