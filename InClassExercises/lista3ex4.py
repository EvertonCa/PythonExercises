print("Digite um numero")
n1=int(input())
print("Digite outro numero")
n2=int(input())
print("Digite outro numero")
n3=int(input())
if(n1>n2 and n1>n3):
	if(n2>n3):
		print("A ordem eh",n1,n2,n3)
	elif(n3>n2):
		print("A ordem eh",n1,n3,n2)
elif(n2>n1 and n2>n3):
	if(n1>n3):
		print("A ordem eh",n2,n1,n3)
	elif(n3>n1):
		print("A ordem eh",n2,n3,n1)
elif(n3>n2 and n3>n2):
	if(n1>n2):
		print("A ordem eh",n3,n1,n2)
	elif(n2>n1):
		print("A ordem eh",n3,n2,n1)