from math import *
n = 5

for col in range(n*2):
    for row in range((n*2)-1):
        if row+col < ceil((n*2)/2):
            print("*", end="\t")
        elif row-col > ceil((n*2)/2)-2:
            print("*", end="\t")
        elif row == (n*2)-2 or col == (n*2)-1 or row == 0:
            print("*", end="\t")
        else:
            print("", end="\t")
    print("")
