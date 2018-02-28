while True:
    try:
        linha,coluna = input().split()
        linha = int(linha)
        coluna = int(coluna)
        matriz = []
        vetAuz = []
        matriz.append('0' * (coluna+2))
        for a in range(linha):
            x = input().split()
            x = '0'+''.join(x)+'0'
            matriz.append(x)
        matriz.append('0'*(coluna+2))
        for lin in range(linha):
            vetAuz = []
            for col in range(coluna):
                i = 0
                if matriz[lin+1][col+1] == '1':
                    vetAuz.append('9')
                else:
                    if matriz[lin + 2][col + 1] == '1':
                        i = i + 1
                    if matriz[lin][col + 1] == '1':
                        i = i + 1
                    if matriz[lin + 1][col + 2] == '1':
                        i = i + 1
                    if matriz[lin + 1][col] == '1':
                        i = i + 1
                    vetAuz.append(str(i))
            print(''.join(vetAuz))

    except:
        break