quant = int(input())
for i in range (quant):
    m1, v1 = input().split(" x ")
    m2, v2 = input().split(" x ")
    m1 = int(m1)
    m2 = int(m2)
    v1 = int(v1)
    v2 = int(v2)
    saldoT1 = m1 + v2
    saldoT2 = m2 + v1
    if(saldoT1>saldoT2):
        print("Time 1")
    elif(saldoT2>saldoT1):
        print("Time 2")
    else:
        if(v2>v1):
            print("Time 1")
        elif(v1>v2):
            print("Time 2")
        else:
            print("Penaltis")
