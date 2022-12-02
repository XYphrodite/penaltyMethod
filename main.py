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


# вектор градиента
def grad(x, n):
    # h — приращение
    h = 0.0001
    x1 = x[0]
    x2 = x[1]
    # поиск производной
    y1 = (foo(x1 + h, x2, n) - foo(x1 - h, x2, n)) / (h * 2)
    y2 = (foo(x1, x2 + h, n) - foo(x1, x2 - h, n)) / (h * 2)
    return [y1, y2]
