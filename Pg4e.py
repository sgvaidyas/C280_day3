def task3():
    n = int(input("Choose a number:\n"))
    pattern = ""
    cnt = 1
    for i in range(1, 2*n+1):
        if i == 1 or i==2*n:
            pattern = (n*2-1) * " *"
        elif i < n:
            pattern = (n-cnt) * " *" + (2*cnt-1)*"  " + (n-cnt) * " *"
            cnt += 1
        else:
            pattern = " *" + (2*n-3)*"  "+ " *"
        print(pattern)

if __name__ == '__main__':
    task3()
