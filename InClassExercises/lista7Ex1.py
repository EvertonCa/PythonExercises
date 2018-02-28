def parOuImpar(num):
    if(num<0):
        return 0
    else:
        return 1
print("Digite um numero:")
n = int(input())
r = parOuImpar(n)
if(r==0):
    print("Numero Negativo")
else:
    print("Numero Positivo")