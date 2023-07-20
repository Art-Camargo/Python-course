x, y, *resto = 1, 2, 3, 4, 5, 6, 7, 8
def soma(*args):
    return sum(list(args))

print(soma(1,2,3,4,5,6,7,8,9), type(soma(1,2,3,4,5,6,7,8,9)))


numero = 1, 2, 4, 6
print(soma(*numero))