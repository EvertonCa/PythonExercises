testes = int(input())
cont1 = 0
cont0 = 0
for a in input().split():
    if (int(a) == 1):
        cont1 +=1
    else:
        cont0 +=1
if(cont0>cont1):
    print("Y")
else:
    print("N")