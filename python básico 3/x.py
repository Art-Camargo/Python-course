size = int(input('Enter a size: (x > 0): '))
while size < 0:
    size = int(input('Enter a size: (x > 0): '))
for i in range(size):
    for j in range(size):
        if i == j or j == (size - 1) - i:
            print('*', end="")
        else:
            print(' ', end="")
    print('', end="\n")