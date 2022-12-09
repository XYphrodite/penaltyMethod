import math
from math import *
import numpy as np
import matplotlib.pyplot as plt
import random

E = 0.01
dlt = E / 100


def fooA(x1, x2):
    a = 1
    b = 1
    c = 1
    d = 3
    alf = 120
    return (pow(((x1 - a) * cos(alf) + (x2 - b) * sin(alf)), 2)) / (c * c) + \
           (pow(((x2 - b) * cos(alf) - (x1 - a) * sin(alf)), 2)) / (d * d)


def fooB(x1, x2):
    return 100 * pow((x2 - pow(x1, 2)), 2) + pow((1 - x1), 2)


def foo(x1, x2, n=0):
    if n == 0:
        return fooA(x1, x2)
    else:
        return fooB(x1, x2)


def f1(x):
    x1 = x[0]
    x2 = x[1]
    return x1 * x2 - (1 / math.pow(math.e, x2))


def f2(x):
    return x[0] + x[1]


def isIn(x):
    if (f1(x) <= 0) and (f2(x) >= 0):
        return True
    else:
        return False


'''
# вектор градиента
def grad(x, n):
    # h — приращение
    h = 0.01
    x1 = x[0]
    x2 = x[1]
    # поиск производной
    y1 = (foo(x1 + h, x2, n) - foo(x1 - h, x2, n)) / (h * 2)
    y2 = (foo(x1, x2 + h, n) - foo(x1, x2 - h, n)) / (h * 2)
    return [y1, y2]
'''


def interior_penalty(e):
    # штраф
    def R(x1, x2):
        return foo(x1, x2) + k / f1([x1, x2]) + k / f2([x1, x2])

    #
    def gradR(x1, x2):
        h = 0.001
        return [(R(x1 + h, x2) - R(x1 - h, x2)) / (h * 2), (R(x1, x2 + h) - R(x1, x2 - h)) / (h * 2)]

    def gradient(x):
        xx = [x[0], x[1], x[2]]
        h = 0.01
        gradvectR = gradR(xx[0], xx[1])
        while pow(gradvectR[0] + gradvectR[1], 2) > e:
            xx[0] = xx[0] - h * gradvectR[0]
            xx[1] = xx[1] - h * gradvectR[1]
            gradvectR = gradR(xx[0], xx[1])
        xx[2] = foo(xx[0], xx[1])
        return xx

    x_list = []
    k = 2
    c = 0.4
    randy = 10
    x = [random.randint(-randy, randy), random.randint(-randy, randy), 0]

    while not isIn(x):
        x = [random.randint(-randy, randy), random.randint(-randy, randy), 0]

    x[2] = foo(x[0], x[1])
    print("Начальные значения x: [", x[0], ",", x[1], "]")
    xn = gradient(x)

    while abs(x[2] - xn[2]) > dlt:
        x = [xn[0], xn[1], xn[2], k]
        k *= c
        x_list.append(x)
        xn = gradient(x)
    if (len(x_list) > 0):
        x_list.pop()
        x = x_list[len(x_list) - 1]

    return x, x_list


e = 0.01
_x, _x_list = interior_penalty(dlt / 2000)
for i in range(len(_x_list)):
    print(i + 1, ". x1 = ", _x_list[i][0], " x2 = ", _x_list[i][1], " f(x1,x2) = ", _x_list[i][2], " r = ", _x_list[i][3])
print("X* = [", _x[0], ", ", _x[1], " ]")

levels = [-0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.10, -0.05, -0.01, 0.0, 0.01, 0.05, 0.10, 0.20, 0.30, 0.4,
          0.5, 0.6, 0.7, 0.8, 0.9]
xg1 = np.arange(-5, 10.250, 0.250)
xg2 = np.arange(-5, 10.250, 0.250)
xg1, xg2 = np.meshgrid(xg1, xg2)
f2 = np.vectorize(fooA)
yg = f2(xg1, xg2)

x1i = np.linspace(5,-5, 100)
x2i = np.linspace(-5, 10.250, 100)
plt.plot(x1i, x2i, color="blue")

x11j, x22j = -2.4, 0
x1j, x2j = [], []
for i in range(38):
    x22j = x11j * x11j - 1 / math.pow(math.e, x11j)
    x1j.append(x11j)
    x2j.append(x22j)
    x11j += 0.1525
plt.plot(x1j, x2j, color="green")

cont = plt.contour(xg1, xg2, yg, levels=30)
plt.plot(_x[0], _x[1], color="red", marker=".")
plt.show()

if(isIn(_x)):
    print("djfl")
