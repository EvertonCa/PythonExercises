vet1 = []; vet2 = []; vet3 = []
for i in range(5):
    print("Digite o",(i+1),"º numero do vetor 1")
    vet1.append(int(input()))
    vet3.append(vet1[i])
    print("Digite o",(i+1),"º numero do vetor 2")
    vet2.append(int(input()))
    vet3.append(vet2[i])
print(vet3)