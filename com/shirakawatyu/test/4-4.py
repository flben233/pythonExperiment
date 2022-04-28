import datetime
import math
import random
import time
import turtle

DISTS = 12000
hits = 0
startTime = time.time()
turtle.tracer(False)
b = math.sqrt(DISTS / 2)
for i in range(1, DISTS + 1):
    if (i / DISTS) * 100 % 10 == 0:
        print("\r" + ("[{:20}".format("#" * int(i / DISTS * 20))) + "]" + str(i / DISTS * 100) + "%", end="")
    x = random.random()
    y = random.random()
    d = math.sqrt(x * x + y * y)
    if d <= 1.0:
        turtle.penup()
        turtle.goto(x * 100, y * 100)
        turtle.pendown()
        turtle.dot(2, 'red')
        hits += 1
    else:
        turtle.penup()
        turtle.goto(x * 100, y * 100)
        turtle.pendown()
        turtle.dot(2, 'blue')
turtle.penup()
turtle.goto(-100, 0)
turtle.write("X07.方律奔")
pi = 4 * (hits / DISTS)
print("\n" + str(pi))
print("运行时间：" + str(int((time.time() - startTime) * 1000)) + "ms")
turtle.done()
