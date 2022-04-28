a = input().split(",")
# import sys
#
# a = sys.argv[1].split(",")
b = eval(a[0])
c = eval(a[1])
for i in range(b, c):
    flag = True
    for j in range(2, i - 1):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i, end=" ")
