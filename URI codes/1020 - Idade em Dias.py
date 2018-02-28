idade = int(input())
anos = idade//365
sobra = idade%365
meses = sobra//30
dias = sobra%30
print("%d ano(s)"%(anos))
print("%d mes(es)"%(meses))
print("%d dia(s)"%(dias))
