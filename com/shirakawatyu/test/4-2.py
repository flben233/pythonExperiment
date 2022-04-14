import random

r = int(random.uniform(1, 30))
n = 0
while True:
    i = eval(input())
    n = n + 1
    if r > i:
        print("遗憾，太小了")
    elif r < i:
        print("遗憾，太大了")
    else:
        print("预测{}次，你猜中了".format(n))
        break
