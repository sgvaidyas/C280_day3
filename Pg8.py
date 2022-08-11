def fibterm(term):
    n1 = 0
    n2 = 1
    if term == 1:
        return n1
    elif term == 2:
        return n1+n2
    else:
        cnt = 2
        while cnt<term:
            n3=n1+n2
            n1=n2
            n2=n3
            cnt+=1
        else:
            return n3

n = int(input("Enter n = "))
t = 1
for i in range(1,n+1):
    print("-".ljust(10)*(n-i),end="")
    for j in range(2*i-1):
        print(str(fibterm(t)).ljust(10),end="")
        t+=1
    print()

