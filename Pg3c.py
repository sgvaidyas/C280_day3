n = int(input("enter number:"))
for i in range(0,2*n-1):
  if(i<n):
    print(n-i, end=" ")
  else:
    print(i-n+2, end = " ")

'''
n=3

i  i<n   else
   n-i    i-n+2
-------------------
0   3
1   2
2   1
3   F       3-3+2=2
4   F       4-3+2=3


'''
