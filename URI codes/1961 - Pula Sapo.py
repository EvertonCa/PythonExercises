pulo, canos = input().split()
pulo = int(pulo)
canos = int(canos)
lista = []
cont = 0
for i in input().split():
    lista.append(i)
for i in range(canos-1):
    aux = lista[i]
    if int(aux)>=int(lista[i+1]):
        if (int(aux)-int(lista[i+1]) > pulo):
            cont = 1
            break
    else:
        if (int(lista[i+1]) - int(aux) > pulo):
            cont = 1
            break

if cont == 1:
    print("GAME OVER")
else:
    print("YOU WIN")