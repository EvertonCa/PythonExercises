matriz = []
matrizR = []
maior = 0
for i in range(2):
    temp = []
    for j in range(2):
        print("Digite o valor do numero correspondente a linha", (i+1),"e coluna",(j+1))
        valor = int(input())
        temp.append(valor)
        if valor > maior:
            maior = valor
    matriz.append(temp)
for k in range(2):
    temp2 = []
    for l in range(2):
        temp2.append(matriz[k][l] * maior)
    matrizR.append(temp2)
print("A matriz resultante, multiplicada pelo maior valor da primeira matriz (",maior,") é")
print(matrizR[0][0], "",matrizR[0][1])
print(matrizR[1][0], "",matrizR[1][1])