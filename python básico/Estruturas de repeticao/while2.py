count =  0
while count < 10:
    print(count)
    count += 1
count = 0
#não usar break, apenas para exemplo
while(count < 10):
    if(count == 2):
        break
    else:
        print(count)
    count += 1
print("\n\n")
#Não usar, também, o continue
count = 0
while(count < 10):
    if(count >= 2 and count <= 5):
        continue
    else:
        print(count)
    count += 1