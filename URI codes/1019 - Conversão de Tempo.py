N = int(input())
horas = int(N//3600)
minutos = int((N%3600)//60)
segundos = int((N%3600)%60)
print("%d:%d:%d"%(horas,minutos,segundos))
