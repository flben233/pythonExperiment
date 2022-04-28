import math


def distance(a, b, x=0, y=0):
    return math.sqrt((a - x) * (a - x) + (b - y) * (b - y))


print("输入")
dot = input()
dots = dot.split(",")
if len(dots) == 2:
    print(distance(eval(dots[0]), eval(dots[1])))
elif len(dots) == 4:
    print(distance(eval(dots[0]), eval(dots[1]), eval(dots[2]), eval(dots[3])))
