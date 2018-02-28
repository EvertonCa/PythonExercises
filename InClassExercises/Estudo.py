a, b ,c = input().split(" ")
a=int(a)
b=int(b)
c=int(c)
if(a>b and a>c):
    if(b>c):
        primeiro = c
        segundo = b
        terceiro = a
    else:
        primeiro = b
        segundo = c
        terceiro = a
elif(b>a and b>c):
    if(a>c):
        primeiro = c
        segundo = a
        terceiro = b
    else:
        primeiro = a
        segundo = c
        terceiro = b
else:
    if(a>b):
        primeiro = b
        segundo = a
        terceiro = c
    else:
        primeiro = a
        segundo = b
        terceiro = c
print(primeiro)
print(segundo)
print(terceiro)
print()
print(a)
print(b)
print(c)
