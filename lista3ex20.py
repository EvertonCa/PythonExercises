print("Digite o codigo do produto - entre 1 e 10.")
codigo=int(input())
print("Digite o peso do produto em quilos.")
peso=float(input())
print("Digite o codigo do pais - entre 1 e 3")
pais=int(input())
gramas=float(peso*1000)
if(codigo>0 and codigo<5):
	preco=gramas*10
elif(codigo>=5 and codigo<=7):
	preco=gramas*25
else:
	preco=gramas*35
if(pais==1):
	imposto=preco*0
elif(pais==2):
	imposto=preco*0.15
else:
	imposto=preco*0.25
print("O peso do produto em gramas eh",gramas)
print("O preco total do produto eh",preco)
print("O valor do imposto eh",imposto)
total=preco+imposto
print("O preco total do produto com imposto eh R$ %.2f"%total)
