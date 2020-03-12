import math


def factorial(x):
    product = 1
    if x < 0:
        return -1
    elif x == 0:
        return 1
    else:
        for i in range(1, x + 1):
            product *= i
        return product


def estimate_pi(accuracy):
    the_sum = 0
    k = 0
    while True:
        the_sum += factorial(4 * k) * (1103 + 26390 * k) / (factorial(k) ** 4 * 396 ** (4 * k))
        if math.fabs(1 / (the_sum * 2 * math.sqrt(2) / 9801) - math.pi < accuracy):
            return 1 / (the_sum * 2 * math.sqrt(2) / 9801)
        k += 1


print(estimate_pi(1e-15))