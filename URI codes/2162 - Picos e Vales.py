quant = int(input())
x = input().split()
x = list(map(int,x))
i = 0
continua = True
while i < (quant - 2) and continua:
    if (x[i] >= x[i+1] and x[i+1] >= x[i+2]) or (x[i] <= x[i+1] and x[i+1] <= x[i+2]):
        continua = False
    i = i + 1
if quant > 2:
    if continua:
        print("1")
    else:
        print("0")
else:
    if x[0] == x[1]:
        print("0")
    else:
        print("1")