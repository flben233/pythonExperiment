x = 888


def foo():
    x = 666
    print("local x:", x)


foo()
print("global x:", x)
