while True:
    try:
        hora, minuto = input().split(":")
        hora = int(hora)
        minuto = int(minuto)
        horaEmMinutos = hora * 60
        minutosTotais = horaEmMinutos + minuto
        if(minutosTotais<=420):
            atrasoMaximo = 0
        else:
            atrasoMaximo = minutosTotais - 420
        print("Atraso maximo: %d"%atrasoMaximo)
    except:
        break