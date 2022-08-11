def myfun(*args):
    print(type(args))
    for x in args:
        print(x)

myfun('name',222,99.6,True)
myfun(11,22)
myfun(1,2,3)
