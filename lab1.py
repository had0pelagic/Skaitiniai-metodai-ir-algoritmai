import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return (0.47*pow(x, 4)) + (1.86 * pow(x, 3)) - (1.01 * pow(x, 2)) - (6.39 * x) - 1.85


t = np.arange(0.0, 10, 0.01)
s = func(t)

fig, ax = plt.subplots()
ax.plot(t, s)
ax.grid()
plt.show()
print(func(1))
