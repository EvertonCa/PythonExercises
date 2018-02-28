valor=1
while(valor>0 and valor<4):
    print("Digite a opcao desejada:")
    print("1. Imposto")
    print("2. Novo salario")
    print("3. Classificacao")
    print("4. Finalizar o programa")
    valor = int(input())
    while(valor<1 or valor>4):
        print("Opcao invalida. Favor digitar novamente")
        valor = int(input())
    if(valor==1):
        print("Digite o salario do funcionario")
        salario = float(input())
        if(salario<500):
            imposto=salario*0.05
        if (salario >= 500 and salario < 850):
            imposto = salario * 0.1
        if (salario >= 850):
            imposto = salario * 0.15
        print("O imposto eh R$%.2f"%imposto)
    if(valor==2):
        print("Digite o salario do funcionario")
        salario = float(input())
        if(salario<450):
            novoSalario = salario + 100
        if (salario >= 750 and salario <= 1500):
            novoSalario = salario + 50
        if (salario >= 450 and salario < 750):
            novoSalario = salario + 75
        if (salario > 1500):
            novoSalario = salario + 25
        print("O novo salario sera R$%.2f"%novoSalario)
    if(valor==3):
        print("Digite o salario do funcionario")
        salario = float(input())
        if(salario<=750):
            print("Mal remunerado")
        if(salario>750):
            print("Bem remunerado")
'''
Integrantes
Markel Macedo RA 22.117.060-8
Everton Cardoso RA 22.117.061-6
Gabriel Venancio RA 22.117.063-2
Guilherme Colla RA 22.117.058-2
Giovanni Vilella RA 22.117.047-5
Artur Silva RA 22.117.076-4
Gustavo Velasco RA 22.117.042-6
'''
