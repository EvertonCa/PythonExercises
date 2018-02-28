valor = []; quant = []
valorMaior = int(0)
valorTotal = int(0)
for i in range(10):
    print("Digite o valor do ", (i+1),"º produto")
    valor.append(int(input()))
    print("Digite a quantidade do ", (i + 1), "º produto")
    quant.append(int(input()))
for j in range(10):
    print("Foram vendidos",quant[j],"itens do",(j+1),"º produto de preço unitario R$", valor[j],", totalizando R$",(quant[j]*valor[j]))
for l in range(10):
    valorTotal = valorTotal + (valor[l]*quant[l])
print("O valor total das vendas foi de R$",valorTotal)
print("A comissão do vendedor será de R$%0.2f"%(0.05*valorTotal))
for k in range(10):
    if(valor[k]>valorMaior):
        valorMaior = valor[k]
        posicao = k+1
print("O maior valor é R$",valorMaior,"localizado na posição",posicao)