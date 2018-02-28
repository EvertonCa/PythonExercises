5contAprovado=0
contReprovado=0
contExame=0
contMedia=0
for i in range(6):
	print ("Digite a n1")
	n1=float(input())
	print ("Digite a n2")
	n2=float(input())
	media=(n1+n2)/2
	if(media<3):
		print("A media do aluno eh",media)
		print("Aluno Reprovado")
		contReprovado=contReprovado+1
	elif(media>=3 and media<7):
		print("A media do aluno eh",media)
		print("Aluno de exame")
		contExame=contExame+1
	elif(media>=7):
		print("A media do aluno eh",media)
		print("Aluno Aprovado")
		contAprovado=contAprovado+1
	contMedia=contMedia+media
print("O total de alunos aprovados eh ",contAprovado)
print("O total de alunos reprovados eh ",contReprovado)
print("O total de alunos em exame eh ",contExame)
mediaSala=contMedia/6
print("A media da classe eh %.2f"%mediaSala)
