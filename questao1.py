# Declaração de funções
def analisa():
    rodada = input().split()
    rodadaint = []
    y = 0
    for l in range(len(rodada)):
        rodadaint.append(int(rodada[l]))  # Converte o valor das jogadas para Inteiro
        y += rodadaint[l]
    partidas.append(jogadores[y % n])
    return None

# Programa principal
partidas = []
n = 1
p = 1
k = 0
while n != 0 and p != 0:
    k += 1
    jogadores = []  # Cria e limpa a lista de jogadores
    entrada = input().split()
    n = int(entrada[0])
    p = int(entrada[1])
    for i in range(n):
        jogadores.append(input())
    partidas = []  # Limpa a lista de resultados das partidas
    for j in range(p):
        analisa()
    if n != 0 and p != 0:
        print("Sequência %d" % k)
    for x in range(len(partidas)):  # Dá o resultado da rodada
        print(partidas[x])
    print()

