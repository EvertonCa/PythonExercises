c = []
x = 0
for i in range(10):
    c.append(int(input()))
    if c[i] >=50:
        print("Foi encontrado o número:",c[i])
        print("Posição:",i)
        x = 1

if x ==0:
    print("Não foi encontrado nenhum número")