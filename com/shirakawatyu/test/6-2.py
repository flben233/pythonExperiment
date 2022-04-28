def max2(a, b):
    if a > b:
        return a
    else:
        return b


def max3(a, b, c):
    if max2(a, b) > c:
        return max2(a, b)
    else:
        return c


t = input()
d = t.split(",")
print(max3(eval(d[0]), eval(d[1]), eval(d[2])))
