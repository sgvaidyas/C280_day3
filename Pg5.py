n = 5
first = True

number1 = 0
number2 = 1

for col in range(n):
    for row in range((n * 2) - 1):
        if row + col < n - 1:  # upper left
            print(".", end="\t")
        elif row - col > n - 1:  # upper right
            print(".", end="\t")
        else:
            if first:
                print("0", end="\t")
                first = not first
            else:
                print(number2, end="\t")
                x = number2
                number2 = number1 + number2
                number1 = x

    print("")
