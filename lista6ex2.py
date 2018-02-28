matriz = []
contador1 = 0
contador2 = 0
contador3 = 0
for i in range(10):
    temp = []
    for j in range(3):
        print("Digite o valor da ", (j+1),"ª nota do ",(i + 1),"º aluno.")
        valor = int(input())
        temp.append(valor)
    matriz.append(temp)
for i in range(10):
    menor = 15
    if matriz[i][0] < menor:
        menor = matriz[i][0]
        indice = 1
    if matriz[i][1] < menor:
        menor = matriz[i][1]
        indice = 2
    if matriz[i][2] < menor:
        menor = matriz[i][2]
        indice = 3
    if indice == 1:
        contador1 = contador1 + 1
    if indice == 2:
        contador2 = contador1 + 1
    if indice == 3:
        contador3 = contador1 + 1
    print("O ", (i + 1), "º aluno teve a ",indice, "ª prova, com nota ",menor," como a pior.")
print("Na primeira prova, ",contador1," alunos tiveram a pior nota")
print("Na segunda prova, ",contador2," alunos tiveram a pior nota")
print("Na terceira prova, ",contador3," alunos tiveram a pior nota")