import math
while True:
    try:
        d, vf, vg = input().split(" ")
        d = int(d)
        vf = int(vf)
        vg = int(vg)
        aux = 12**2 + d**2
        hip = math.sqrt(aux)
        tempoF = float(12/vf)
        tempoG = float(hip/vg)
        if(tempoF>=tempoG):
            print("S")
        else:
            print("N")
    except:
        break