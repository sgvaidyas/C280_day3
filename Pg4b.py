num = int(input("Enter the number: "))

for row in range(1,(num*2)+1):
    for col in range(1, (num*2)):
        if row + col <= num+1 :
            print("*", end="\t")
        elif col - row >= num-1 :
            print("*", end="\t")
        elif col == 1 or col == num*2-1:
            print("*", end="\t")
        elif row == num*2 :
            print("*", end="\t")
        else:
            print(" \t",end="")
    print()
