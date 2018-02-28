def armazena(x,y):
    x.append(y)

def media():
    p=0
    u=0
    soma=0
    for a in vCab:
        if a == 'P' or a == 'C':
            soma = soma + vId[p]
            u = u + 1
        p = p + 1
    if u == 0:
        u=1
    return soma/u

def maiorIdade():
    vId.sort()
    return vId[len(vId)-1]

def fem():
    n = 0
    m = 0
    for r in vSexo:
        if r == 'feminino':
            if vId[m] >= 18 and vId[m] <= 35 and vCab[m] == 'L' and vOlho[m] == 'A':
                n = n + 1
        m = m + 1
    return n

i = 1
vSexo = []
vOlho = []
vCab = []
vId = []
while i <= 5:
    sx = input("Digite o sexo")
    armazena(vSexo,sx)
    olho = input("Digite a cor dos olhos")
    armazena(vOlho,olho)
    cab = input("Digite a cor do cabelho")
    armazena(vCab,cab)
    id = int(input("Digite a idade"))
    armazena(vId,id)
    i = i + 1

print("Media das idades %.2f" %media())
print("Maior idade %d" %maiorIdade())
print("A quantidade de pessoas do sexo feminino com idade entre 18 e 35 anos e de olhos azuis e cabelos loiros é",fem())