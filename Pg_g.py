def function17():
    n1=5
    n=n1+1
    count=0
    turn=n1*2-1
    while count<turn:
        print("out count = ",count)
        count=count+1
        while n>=1:
            n=n-1
            print(n,end=" ")
            if n==1:
                while n!=n1:
                    n=n+1
                    print(n,end=" ")
                    count+=1
                else:
                    break
            elif  count<=turn:
                # print(n," ",count," ",turn)
                break
if __name__=="__main__":
    function17()
