import math

e = 1


def compute_e(n):
    global e
    e = e + 1 / math.factorial(n)
    n -= 1
    if n == 0:
        return e
    else:
        return compute_e(n)


def calculate2_e(n):
    global e
    for i in range(1, n + 1):
        e += 1 / math.factorial(i)
    return e


print(compute_e(6))
