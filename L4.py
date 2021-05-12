import numpy as np
import matplotlib.pyplot as plt
import os
import time
from scipy.integrate import odeint

plt.style.use('bmh')
os.system("cls")


def R(h):  # spindulys atitinkamam aukstyje
    return 0.3*np.sqrt(abs(h))+0.005


def dh(a_w, a_h, h):  # dif lygtis
    return -((c*a_h)/a_w)*np.sqrt(2*g*abs(h))


def Euler(r_h, c, h_0, t_max, r_c, g, step):
    a_h = np.pi*r_h**2  # vazos ertmes skers plotas nekinta
    a_w_s = np.pi*r_c**2  # cilindro skers plotas
    done_at = -1
    done_at_s = -1
    h = []
    h_s = []
    h.append(h_0)
    h_s.append(h_0)

    x = np.arange(0, t_max)

    for t in x[1:]:
        a_w = np.pi*R(h[t-1])**2  # vazos skers plotas
        h.append(h[t-1] + step*dh(a_w, a_h, h[t-1]))
        h_s.append(h_s[t-1] + step*dh(a_w_s, a_h, h_s[t-1]))  # cilindro

        if (h[t] < 0 and done_at == -1):
            done_at = t
        if (h_s[t] < 0 and done_at_s == -1):
            done_at_s = t

    fig = plt.figure()
    ax = fig.add_subplot()
    plt.title("Euler")
    ax.plot(x, h, label="vaza6", color="green")
    for i in h:
        print(str(i))
    ax.plot(x, h_s, label="cilindras", color="red")
    plt.axvline(done_at, color="green", linewidth="0.5")
    plt.axvline(done_at_s, color="red", linewidth="0.5")
    plt.axhline(0, color="black", linewidth="0.5")
    plt.xlabel("laikas (s)")
    plt.ylabel("aukstis h")
    plt.legend()
    print("vaza istustejo per: " + str(done_at) + " s")
    print("cilindras istustejo per: " + str(done_at_s) + " s")
    plt.show()


def Euler_multi(r_h, c, h_0, t_max, g, steps):
    steps = [1, 2, 4, 8, 32]
    for step in steps:
        a_h = np.pi*r_h**2
        done_at = -1
        h = []
        h.append(h_0)
        x = np.arange(0, t_max)
        for t in x[1:]:
            a_w = np.pi*R(h[t-1])**2
            h.append(h[t-1] + step*dh(a_w, a_h, h[t-1]))
            if (h[t] < 0 and done_at == -1):
                done_at = t

        plt.title("Euler daug zingsniu")
        print(h)
        print("-------------")
        plt.plot(x, h, label=f'vaza6 step = {step}')
        plt.axvline(done_at, linewidth="0.5")
        plt.axhline(0, color="black", linewidth="0.5")
        plt.xlabel("laikas (s)")
        plt.ylabel("aukstis h")
        plt.legend()
        print("vaza istustejo per: " + str(done_at) + " s")

    plt.show()


def rk4_multi(r_h, c, h_0, t_max, r_c, g, steps):

    for step in steps:
        a_h = np.pi*r_h**2
        done_at = -1
        h = []
        h.append(h_0)
        x = np.arange(0, t_max)
        for t in x[1:]:

            a_w = np.pi*R(h[t-1])**2
            ys = h[t-1] + step / 2 * dh(a_w, a_h, h[t-1])

            a_ww = np.pi*R(ys)**2
            yss = h[t-1] + step / 2 * dh(a_ww, a_h, ys)

            a_www = np.pi*R(yss)**2
            ysss = h[t-1] + step * dh(a_www, a_h, yss)

            a_wwww = np.pi*R(ysss)**2

            h.append(h[t-1] + (step / 6) * (dh(a_w, a_h, h[t-1]) + 2 *
                                            dh(a_ww, a_h, ys) + 2 * dh(a_www, a_h, yss) + dh(a_wwww, a_h, ysss)))

            if (h[t] < 0 and done_at == -1):
                done_at = t

        plt.title("Daug zingsniu rk4")
        print(h)
        print("-------------")
        plt.plot(x, h, label=f'vaza6 step = {step}')
        plt.axvline(done_at, linewidth="0.5")
        plt.axhline(0, color="black", linewidth="0.5")
        plt.xlabel("laikas (s)")
        plt.ylabel("aukstis h")
        plt.legend()
        print("vaza istustejo per: " + str(done_at) + " s")
    plt.show()


def rk4(r_h, c, h_0, t_max, r_c, g, step):
    a_h = np.pi*r_h**2  # vazos ertmes skers plotas nekinta
    a_w_s = np.pi*r_c**2  # cilindro skers plotas
    done_at = -1
    done_at_s = -1
    h = []
    h_s = []
    h.append(h_0)
    h_s.append(h_0)

    x = np.arange(0, t_max)
    for t in x[1:]:

        a_w = np.pi * R(h[t-1]) ** 2
        ys = h[t-1] + step / 2 * dh(a_w, a_h, h[t-1])

        a_ww = np.pi * R(ys) ** 2
        yss = h[t-1] + step / 2 * dh(a_ww, a_h, ys)

        a_www = np.pi * R(yss) ** 2
        ysss = h[t-1] + step * dh(a_www, a_h, yss)

        a_wwww = np.pi * R(ysss) ** 2
        h.append(h[t-1] + (step / 6) * (dh(a_w, a_h, h[t-1]) + 2 * dh(a_ww,
                                                                      a_h, ys) + 2 * dh(a_www, a_h, yss) + dh(a_wwww, a_h, ysss)))
        # cil
        ys_s = h_s[t-1] + step / 2 * dh(a_w_s, a_h, h_s[t-1])
        yss_s = h_s[t-1] + step / 2 * dh(a_w_s, a_h, ys_s)
        ysss_s = h_s[t-1] + step * dh(a_w_s, a_h, yss_s)
        h_s.append(h_s[t-1] + (step / 6) * (dh(a_w_s, a_h, h_s[t-1]) + 2 *
                                            dh(a_w_s, a_h, ys) + 2 * dh(a_w_s, a_h, yss) + dh(a_w_s, a_h, ysss)))
        if (h[t] < 0 and done_at == -1):
            done_at = t

        if (h_s[t] < 0 and done_at_s == -1):
            done_at_s = t

    fig = plt.figure()
    ax = fig.add_subplot()
    plt.title("rk4 Vienas zingsnis")
    ax.plot(x, h, label="vaza6", color="green")
    # print(h_s)
    for i in h:
        print(str(i))
    ax.plot(x, h_s, label="cilindras", color="red")
    plt.axvline(done_at, color="green", linewidth="0.5")
    plt.axvline(done_at_s, color="red", linewidth="0.5")
    plt.axhline(0, color="black", linewidth="0.5")
    plt.xlabel("laikas (s)")
    plt.ylabel("aukstis h")
    plt.legend()
    print("vaza istustejo per: " + str(done_at) + " s")
    print("cilindras istustejo per: " + str(done_at_s) + " s")
    plt.show()


r_h = 0.005  # ertmes spindulys
c = 0.6  # proporcingumo daugiklis
h_0 = 0.25  # pradinio laiko momentu skyscio aukstis inde
t_max = 140  # t0 pradinis laiko momentas tmax galinis
r_c = 0.09  # lyginimui spindulys
g = 9.8
step = 8

steps = [1, 2, 4, 8, 16, 32]

Euler(r_h, c, h_0, t_max, r_c, g, step)
# Euler_multi(r_h, c, h_0, t_max, g, steps)
# rk4(r_h, c, h_0, t_max, r_c, g, step)
# rk4_multi(r_h, c, h_0, t_max, r_c, g, steps)
