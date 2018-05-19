import math


def solve_quadratic_equation(a, b, c):
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return x1, x2
    elif discr == 0:
        x3 = -b / (2 * a)
        x4 = None
        return x3, x4
    elif discr < 0:
        x5 = None
        x6 = None
        return x5, x6

print(solve_quadratic_equation(3, 1, 5))