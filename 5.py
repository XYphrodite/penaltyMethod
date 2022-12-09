from math import *
import numpy as np
import matplotlib.pyplot as plt
import random


def f(x1, x2):
    a = -3
    b = -1
    c = 1
    d = 3
    alf = 130
    return (pow(((x1 - a) * cos(alf) + (x2 - b) * sin(alf)), 2)) / (c * c) + \
           (pow(((x2 - b) * cos(alf) - (x1 - a) * sin(alf)), 2)) / (d * d)


def con1(x1, x2):
    return pow(x1, 2) + 2 * x2


def con2(x1, x2):
    return x2 - x1


def in_constraints(X):
    if (con1(X[0], X[1]) <= 0) and (con2(X[0], X[1]) == 0):
        return True
    else:
        return False


def interior_penalty(e):
    def R(x1, x2):
        return f(x1, x2) + k * (pow(max(0.0, -con1(x1, x2)), 5) + pow((con1(x1, x2)), 5))

    def gradR(x1, x2):
        h = 0.01
        return [(R(x1 + h, x2) - R(x1 - h, x2)) / (h * 2), (R(x1, x2 + h) - R(x1, x2 - h)) / (h * 2)]

    def gradient(xi):
        xx = xi.copy()
        h = 1
        gradvectR = gradR(xx[0], xx[1])
        N = 0
        while pow(gradvectR[0] + gradvectR[1], 2) > e and N < 1000:
            xx[0] = xx[0] - h * gradvectR[0]
            xx[1] = xx[1] - h * gradvectR[1]
            gradvectR = gradR(xx[0], xx[1])
            N += 1
            # print(x, " ", xx, " ", k)
            # print("help 3 ", xx, "vctr ", gradvectR)
        xx[2] = f(xx[0], xx[1])
        return xx

    x_list = []
    k = 1
    c = 0.5
    randy = 100
    x1 = random.randint(-randy, randy)
    x2 = random.randint(-randy, randy)
    '''
    while not in_constraints([x1, x2]):
        x1 = random.randint(-randy, randy)
        x2 = 6 - 3 * x1
        print('wver')
        '''
    x = [x1, x2, 0]
    # x = [1, 1, 0]

    x[2] = f(x[0], x[1])
    print("Initial x: ", x)
    xn = gradient(x)

    while abs(x[2] - xn[2]) > e:
        # print("help 2")
        k *= c
        x = xn.copy()
        x_list.append(x)
        xn = gradient(x)

    return x, x_list


e = 0.000001
_x, _x_list = interior_penalty(e)
for i in range(len(_x_list)):
    print(i + 1, ". x1: ", _x_list[i][0], " x2: ", _x_list[i][1], " y: ", _x_list[i][2], " k: ")
print("Solution: ", _x[0], " ", _x[1])

if con1(_x[0], _x[1]) <= 0:
    print("YEEEEEEEEEEEEEEES")

levels = [-0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.10, -0.05, -0.01, 0.0, 0.01, 0.05, 0.10, 0.20, 0.30, 0.4,
          0.5, 0.6, 0.7, 0.8, 0.9]
xg1 = np.arange(-10, 10.250, 0.250)
xg2 = np.arange(-10, 10.250, 0.250)
xg1, xg2 = np.meshgrid(xg1, xg2)
f2 = np.vectorize(f)
yg = f2(xg1, xg2)

x11i, x22i = -10, -10
x1i, x2i = [], []

x11j, x22j = -5, -5
x1j, x2j = [], []

for i in range(100):
    x22i = -54 / x11i
    x22j = 6 - 3 * x11i

    if x22i > 10:
        x22i = 10
    if x22i < -10:
        x22i = -10
    if x22j > 10:
        x22j = 10
    if x22j < -10:
        x22j = -10

    x1i.append(x11i)
    x2i.append(x22i)
    x1j.append(x11i)
    x2j.append(x22j)

    x11i += 0.1525

plt.plot(x1i, x2i, color="blue")

plt.plot(x1j, x2j, color="green")

cont = plt.contour(xg1, xg2, yg, levels=30)
plt.plot(_x[0], _x[1], color="red", marker=".")
plt.show()
