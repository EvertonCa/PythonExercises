x = input()
cont=0
for i in x:
    if i == '1':
        cont = cont + 1
if cont%2 == 0:
    print("%s0"%x)
else:
    print("%s1"%x)