import math


def factorial(n):
    b = 1
    for i in range(1, n):
        b *= i
    return b


j = 1
e = 0
t = math.pow(10, -6)
while True:
    a = 1 / factorial(j)
    e += a
    if a < t:
        break
    j += 1
print(e)
