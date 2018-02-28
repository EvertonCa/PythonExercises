i = 1
nome = []
tempo = []
salario = []
aumento = []
Naumento = []
NovoSalario = []
while i <= 5:
    a = input("Digite o nome do funcionario:\n ")
    b = float(input("Digite o salario do funcionario:\n"))
    c = float(input("Digite o tempo de servico em anos do funcionario:\n"))
    nome.append(a)
    salario.append(b)
    tempo.append(c)
    i = i + 1
i = 0
while i < 5:
    if tempo[i] > 5 or salario[i] < 400:
        aumento.append(nome[i])
    else:
        Naumento.append(nome[i])
    i = i + 1
print("Funcionarios que terao aumento",aumento)
print("Funcionarios que nao terao aumento",Naumento)
i = 0
j=0
while i < 5:
    if tempo[i] > 5 or salario[i] < 400:
        if tempo[i] > 5 and salario[i] < 400:
            NovoSalario.append(salario[i] * 1.35)
        elif tempo[i] > 5 and salario[i] >= 400:
            NovoSalario.append(salario[i] * 1.25)
        elif tempo[i] < 5 and salario[i] < 400:
            NovoSalario.append(salario[i] * 1.15)
        print("Funcionario %s tera um novo salario de %.2f" %(aumento[j],NovoSalario[j]))
        j = j + 1

    i = i + 1

