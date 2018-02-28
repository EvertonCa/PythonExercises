import math
a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)
maiorAB = int((a+b+(math.fabs(a-b)))/2)
maior = int((maiorAB+c+(math.fabs(maiorAB-c)))/2)
print(maior,"eh o maior")
