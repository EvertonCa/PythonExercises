t=int(input())
for i in range (t):
    bonus=int(input())
    a1, d1, l1 = input().split(" ")
    a2, d2, l2 = input().split(" ")
    a1=int(a1)
    a2=int(a2)
    d1=int(d1)
    d2=int(d2)
    l1=int(l1)
    l2=int(l2)
    if(l1%2==0):
        golpe1=((a1+d1)/2)+bonus
    else:
        golpe1=((a1+d1)/2)
    if(l2%2==0):
        golpe2=((a2+d2)/2)+bonus
    else:
        golpe2=((a2+d2)/2)
    if(golpe1>golpe2):
        print("Dabriel")
    elif(golpe2>golpe1):
        print("Guarte")
    else:
        print("Empate")
