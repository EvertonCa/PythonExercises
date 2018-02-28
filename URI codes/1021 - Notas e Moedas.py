notas, moedas = input().split(".")
notas = int(notas)
moedas = int(moedas)
cem = notas//100
sobra = notas%100
cinquenta = sobra//50
sobra = sobra%50
vinte = sobra//20
sobra = sobra%20
dez = sobra//10
sobra = sobra%10
cinco = sobra//5
sobra = sobra%5
dois = sobra//2
um = sobra%2
	
cents50 = moedas//50
sobra = moedas%50
cents25 = sobra//25
sobra = sobra%25
cents10 = sobra//10
sobra = sobra%10
cents5 = sobra//5
sobra = sobra%5
cent1 = sobra//1

print("NOTAS:");
print("%d nota(s) de R$ 100.00"%(cem))
print("%d nota(s) de R$ 50.00"%(cinquenta))
print("%d nota(s) de R$ 20.00"%(vinte))
print("%d nota(s) de R$ 10.00"%(dez))
print("%d nota(s) de R$ 5.00"%(cinco))
print("%d nota(s) de R$ 2.00"%(dois))
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00"%(um))
print("%d moeda(s) de R$ 0.50"%(cents50))
print("%d moeda(s) de R$ 0.25"%(cents25))
print("%d moeda(s) de R$ 0.10"%(cents10))
print("%d moeda(s) de R$ 0.05"%(cents5))
print("%d moeda(s) de R$ 0.01"%(cent1))
