modelo = []; consumo = []
maior = int(0)
for i in range(5):
    print("Digite o modelo do",(i+1),"º veículo.")
    modelo.append(input())
    print("Digite o consumo do",(i+1),"º veículo.")
    consumo.append(int(input()))
    if consumo[i]>maior:
        maior = consumo[i]
        melhor = int(i)
print("O carro mais econômico é o",modelo[melhor],"fazendo",consumo[melhor],"km/l.")
for i in range(5):
    print("O modelo",modelo[i],"gastará %0.2f"%(1000/consumo[i]),"litros para percorrer 1000 km")
