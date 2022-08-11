n = int(input("Enter the n = "))

for i in range(1,2*n):
    if i<=n:
        print(" "*(n-i),end="")
    else:
        print(" "*(i-n),end="")
    j = 1
    p=True
    x = (2*n)-i
    while( (i >= j >=1 and i<=n) or (x>=j>=1) ):
        print(j,end="")
        if p:
            j+=1
        else:
            j-=1
        if j>i or j>x:
            p=False
            j-=2
    print()
