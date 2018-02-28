contVeiculos=0
contAcidentes=0
cont=0
for i in range(1,6):
	print("Digite o codigo da",i,"ª cidade:")
	codigoCidade=int(input())
	print("Digite o numero de veiculos da",i,"ª cidade:")
	numVeiculos = int(input())
	print("Digite o numero de acidentes da",i,"ª cidade:")
	numAcidentes=int(input())
	if(i==1):
		menorIndice=numAcidentes
		maiorIndice=numAcidentes
		menorCidade=codigoCidade
		maiorCidade=codigoCidade
	elif(numAcidentes>maiorIndice):
		maiorIndice=numAcidentes
		maiorCidade=codigoCidade
	elif(numAcidentes<menorIndice):
		menorIndice=numAcidentes
		menorCidade=codigoCidade
	contVeiculos=contVeiculos+numVeiculos
	if(numVeiculos<2000):
		contAcidentes=contAcidentes+numAcidentes
		cont=cont+1
mediaVeiculos=contVeiculos/5
mediaAcidentes=contAcidentes/cont
print("O maior indice de acidentes eh",maiorIndice,"e pertence a cidade de codigo",maiorCidade)
print("O menos indice de acidentes eh",menorIndice,"e pertence a cidade de codigo",menorCidade)
print("A media de veiculos eh",mediaVeiculos)
print("A media de acidentes em cidades com menos de 2000 veiculos eh",mediaAcidentes)