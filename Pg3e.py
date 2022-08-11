def task2():
    n = int(input("Choose a number:\n"))
    print(n, end=" ")
    n1 = n
    n-=1
    backwards = 1
    while n != n1+1:
        if n == 1 or backwards == 0:
            backwards = 0
            print(n, end=" ")
            n += 1
        else:
            print(n, end=" ")
            n -= 1

if __name__ == '__main__':
    task2()
