n = int(input("Enter a number: "))

for row in range(1, (n * 2) + 1):
    for col in range(1, n * 2):
        if row + col <= n + 1 or col - row >= n - 1 or row + col == n * 5 + 1 \
                or col == 1 or col == n * 2 - 1 or row == n * 2:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
