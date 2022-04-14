k = 0
for i in range(1, 200):
    if i == 8:
        print("{:>10d}".format(i), end="")
        k = k + 1
    else:
        if i % 10 == 8:
            if k % 4 == 0 and k != 0:
                print("")
            print("{:>10d}".format(i), end="")
            k = k + 1
