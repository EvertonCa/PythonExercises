positivo = []
negativo = []
for i in range(8):
    print("Digite o ", (i+1),"º número")
    num=int(input())
    if(num<0):
        negativo.append(num)
    else:
        positivo.append(num)
print(positivo)
print(negativo)