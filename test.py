i=5
j=1
p=True
while( i >= j >=1):
    print(j,end="")
    if p:
        j+=1
    else:
        j-=1
    if j>i:
        p=False
        j-=2

