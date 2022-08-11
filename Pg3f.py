n = int(input("Please enter n value: "))
#loop breakers
c = 0
v=0
#storing n in temp var because we will be changing it
temp = n
while c == 0:
    if n == 1:
        print(n,end="")
        c=1
    elif v != 1 :
        print(temp,end="")
        temp-=1
        if temp== 0:
            temp+=1
            v =1
    else:
        temp+=1
        print(temp,end="")
        if temp ==n:
            c = 1
