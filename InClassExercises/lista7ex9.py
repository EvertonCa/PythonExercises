def maiorMenor():
    n.sort()
    print("Maior numero: %d\nMenor numero: %d" % (n[4], n[0]))

print("Digite 5 números inteiros (separados por espaço):")
n = [int(x) for x in input().split(' ')]
maiorMenor()
