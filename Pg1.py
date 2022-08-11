n = int(input("Enter the val of n = "))
n1 = n
cnt = 0
while(n1!=0):
    n1 = n1//10
    cnt+=1
n1=n
sum = 0
while n1!=0:
    r = n1%10
    sum += r**cnt
    n1=n1//10
if n==sum:
	print("ARMSTRONG")
else:
	print("NOT ARMSTRONG")












'''
n = 153 => 1**3+5**3+27 =

============================
n = 153
n1 = n
cnt = 3
sum = 0
n      r=n1%10   sum +=r**3          n1=n1//10
----------------------------------------------------
153      3       sum += r**3=27     15
15       5       sum = 27+125=152   1
1        1       sum = 152+1=153    0
--------------------------------------- 0

if n==sum:
	print("ARMSTRONG")
else:
	print("NOT ARMSTRONG")


'''
