quant = int(input())
for j in range (quant):
    valor = int(input())
    controle = 1
    for i in range (1, valor+1):
        if(i==1):
            s = 1
            controle = controle + 1
        elif(controle % 2 == 0):
            s = s - 1
            controle = controle + 1
        else:
            s = s + 1
            controle = controle + 1
    print(s)