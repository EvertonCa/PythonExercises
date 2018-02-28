def media(x, y, z, letra):
    if letra=="A":
        media = (x+y+z)/3
    else:
        media = (x*0.5+y*0.3+z*0.2)
    return media

print("Digite n1: ")
a = float(input())
print("Digite n2: ")
b = float(input())
print("Digite n3: ")
c = float(input())
print("Digite letra: ")
L = input()

r = media(a, b, c, L )
print(r)
