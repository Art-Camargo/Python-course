from time import sleep
import os
delay = 1
for i in range(24):
    for j in range(60):
        for k in range(60):
            print('hour | minute | second')
            print('-----X--------X-------')
            print('{:.1f}:    {:.1f}:     {:.1f}'.format(i, j, k))
            sleep(delay)
            os.system("cls")