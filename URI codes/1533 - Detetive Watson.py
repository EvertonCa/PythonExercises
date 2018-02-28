def converte(lista):
    nova=[]
    for i in range (len(lista)):
        aux = int(lista[i])
        nova.append(aux)
    return nova

testes = int(input())
while testes != 0:
    x = []
    testes = 1
    maior = 0
    segundoMaior = 0
    x = input().split()
    nova = converte(x)
    for j in range(len(nova)):
        if nova[j] > maior:
            indice = int(j)
            maior = int(nova[j])
    for k in range(len(nova)):
        if (nova[k] > segundoMaior) and (nova[k] < maior):
            indice = k
            segundoMaior = nova[k]
    print(indice + 1)
    testes = int(input())