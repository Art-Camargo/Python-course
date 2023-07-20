size = int(input('Enter a size (odd and greater than 0): '))
while size < 0 or size%2==0:
    size = int(input('Enter a size (odd and greater than 0 ): '))
aux = 1
aux2 = size - 2
for i in range(0, size, 1):
    for j in range(0, size, 1):
        if i <= size // 2:
            if j >= (size // 2) - i and j <= (size // 2) + i:
                print('* ', end="")
            else:
                print('  ', end="")
        else:
            if i == (size // 2) + 1:
                if j >= aux and j <= aux2:
                    print('* ', end="")
                else:
                    print('  ', end="")
            else:
                if j == 0:
                    aux += 1
                    aux2 -= 1    
                if j >= aux and j <= aux2:
                    print('* ', end="")
                else:
                    print('  ', end="")     
    print('', end="\n")        