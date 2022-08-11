terms = int(input("Enter number of terms"))
n1 = 0
n2 = 1
if terms == 1:
    print(n1)
else:
    cnt = 2
    print(n1,n2,end=" ")
    while cnt<terms:
        n3=n1+n2
        print(n3,end=" ")
        n1=n2
        n2=n3
        cnt+=1
