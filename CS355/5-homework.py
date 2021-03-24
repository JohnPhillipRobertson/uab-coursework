import numpy as np
from random import randint, random
import matplotlib.pyplot as mpl
from math import exp

# Problem 5, Triangle
"""
Consider a triangle and a point chosen within the triangle according to the uniform probability law. Let X be the distance from the point to the base of the triangle. Given the height of the triangle, find the CDF and the PDF of X.
"""


def under_me(first, second, randy):
    f_of_x = (second[1] - first[1]) + ((second[1] - first[1]) /
                                       (second[0] - first[0])) * (randy[0] - second[0] - first[0])
    return randy[1] - f_of_x > 0


def triangle(x):
    point_or = (0.0, 0.0)
    point_top = (1.0, 0.0)
    point_var = (x, 1.0)
    rand_point = (random(), random())
    if under_me(point_or, point_top, rand_point) and under_me(point_top, point_var, rand_point) and under_me(point_var, point_or, rand_point):
        return rand_point
    return (0, 0)


for i in range(0):
    mpl.scatter(*triangle(0.0), c="red")
    mpl.scatter(*triangle(0.5), c="green")
    mpl.scatter(*triangle(1.0), c="blue")
# mpl.show()


# Problem 6, Jane
"""
Calamity Jane goes to the bank to make a withdrawal, and is equally likely to find 0 or 1 customers ahead of her. The service time of the customer ahead, if present, is exponentially distributed with parameter [lambda]. What is the CDF of Jane's waiting time?
"""


def cdf_exp(lamb, x):
    out = 1 - exp(-lamb * x)
    return out

# Got help from a tutor from the math tutoring lab


def wait(lamb, rang):
    ahead = randint(0, 1)
    y = rang
    x = 0.5 + cdf_exp(lamb, y)*0.5
    for i in range(rang):
        if int(cdf_exp(lamb, ahead)) == 1:
            y -= 1
    return (y, -x)


for i in range(50):
    for j in [(1, "purple"), (10, "green"), (30, "red"), (60, "black")]:
        mpl.scatter(*wait(j[0], i), c=j[1])

mpl.show()


# Hypotheses:
"""
For 5, the results should be the same for 0 and 1,
because they are right triangles of the same size.

For 6, a CDF ought to look like an upward curve
