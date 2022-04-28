a = input().split(",")
# import sys
#
# a = sys.argv[1].split(",")
b = eval(a[0])
c = eval(a[1])
d = [0 for i in range(c + 2)]
for i in range(1, c + 1):
    if d[i] == 1 or i == 1:
        continue
    k = 2
    j = k * i
    while j <= c:
        if d[j] == 1:
            k += 1
            j = k * i
            continue
        d[j] = 1
        k += 1
        j = k * i
for i in range(b, c + 1):
    if d[i] != 1:
        print(i, end=" ")
