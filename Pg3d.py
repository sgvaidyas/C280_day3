n = 7
n1 = n
reverse = False
while n1 <= n:
    print(n1, end=" ")
    if n1 == 1:
        reverse = True
    if reverse:
        n1 += 1
    else:
        n1 -= 1
'''
n=3
n1 = 3
rev = F

n1<=n   print n1==1  if rev   else
         n1   rev=T   n1+=1   n1-=1
===================================
3<=3 T   3       -      -     2
2<=3 T   2      -        -    1
1<=3 T   1    rev=T    1+1=2  -
2<=3 T   2             2+1=3  -
3<=3 T   3     -        4
========================================>
--------------------------
3 2 1 2 3

'''
