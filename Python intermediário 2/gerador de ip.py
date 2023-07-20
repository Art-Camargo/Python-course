import random

lista = [(f'{random.randint(0, 300)}.{random.randint(0, 300)}.{random.randint(0, 300)}.{random.randint(0, 300)}') for _ in range(20)]
for ips in lista:
    print(ips)