import random

def letra_para_indice(letra):
    return ord(letra.upper()) - ord('A')

def indice_para_letra(indice):
    return chr(indice + ord('A'))

def exibir_matriz(matriz, num_vertices):
    print("\nMatriz:")
    
    letras = [indice_para_letra(i) for i in range(num_vertices)]

    # Topoi
    print("ori→", end="")
    for letra in letras:
        print(f"{letra:>4}", end="")
    print()

    # Separador
    print("dest↓  " + "----" * num_vertices)

    for i in range(num_vertices):
        print(f"  {letras[i]} |", end="")
        for j in range(num_vertices):
            valor = matriz[i][j]
            if valor == 0:
                print("  - ", end="")
            else:
                print(f"{valor:4}", end="")
        print()

def dijkstra(matriz, origem, destino, num_vertices):
    distancias = [float('inf')] * num_vertices
    visitados = [False] * num_vertices
    anteriores = [None] * num_vertices

    origem_idx = letra_para_indice(origem)
    destino_idx = letra_para_indice(destino)
    distancias[origem_idx] = 0

    while True:
        min_dist = float('inf')
        u = -1
        for i in range(num_vertices):
            if not visitados[i] and distancias[i] < min_dist:
                min_dist = distancias[i]
                u = i

        if u == -1 or u == destino_idx:
            break

        visitados[u] = True

        for v in range(num_vertices):
            if matriz[u][v] > 0 and not visitados[v]:
                nova_dist = distancias[u] + matriz[u][v]
                if nova_dist < distancias[v]:
                    distancias[v] = nova_dist
                    anteriores[v] = u

    return distancias[destino_idx], refaz_caminho(anteriores, destino_idx)

def refaz_caminho(anteriores, destino_idx):
    caminho = []
    atual = destino_idx
    while atual is not None:
        caminho.insert(0, indice_para_letra(atual))
        atual = anteriores[atual]
    return caminho
    # Escolhe valor vertices
def grafo_aleat():
    while True:
        try:
            num_vertices = int(input("Número de vértices(2 à 26): "))
            if 2 <= num_vertices <= 26:
                break
            else:
                print("Número inválido.")
        except ValueError:
            print("Digite apenas números inteiros.")

    matriz = [[0] * num_vertices for _ in range(num_vertices)]
    # Coloca valor aleatorio
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if random.choice([True, False]):
                peso = random.randint(1, 36)
                peso2 = random.randint(1, 36)
                matriz[i][j] = peso
                matriz[j][i] = peso2

    # diagonal 0
    for i in range(num_vertices):
        matriz[i][i] = 0

    return matriz, num_vertices

# Modo
while True:
    modo = input("Deseja fazer um grafo aleatório ou manual?\nDigite 'a' para automático ou 'm' para manual: ").lower()
    if modo in ['a', 'm']:
        break
    print("Digite apenas a ou m.")

# checa se ta automático
if modo == 'a':
    matriz, num_vertices = grafo_aleat()
    print(f"\n🔧 Grafo aleatório gerado com {num_vertices} vértices.")
    exibir_matriz(matriz, num_vertices)

# checa se tá manual
else:
    while True:
        try:
            num_vertices = int(input("Quantidade de vértices (máx 26): "))
            if 1 <= num_vertices <= 26:
                break
            else:
                print("Número inválido.")
        except ValueError:
            print("Digite apenas números inteiros.")

    matriz = [[0] * num_vertices for _ in range(num_vertices)]
    for i in range(num_vertices):
        matriz[i][i] = 0

    exibir_matriz(matriz, num_vertices)

    print("\nDigite as arestas no formato: origem destino peso (ex: A B 1). Digite 'fim' para encerrar.")
    while True:
        entrada = input("Aresta: ")
        if entrada.lower() == 'fim':
            break

        partes = entrada.strip().split()
        if len(partes) != 3:
            print("Formato inválido. Use o formato: origem destino peso (ex: A B 1)")
            continue

        origem, destino, peso = partes
        origem = origem.upper()
        destino = destino.upper()

        vertices_validos = [indice_para_letra(i) for i in range(num_vertices)]
        if origem not in vertices_validos or destino not in vertices_validos:
            print(f"Vértice indisponível. Vértice escolhido deve estar entre: {', '.join(vertices_validos)}")
            continue

        if origem == destino:
            print("Não é possível alterar a diagonal principal. (Ex: A A 1)")
            continue

        try:
            peso = int(peso)
            if peso < 0:
                print("Peso inválido. Peso deve ser positivo.")
                continue
        except ValueError:
            print("Digite apenas números inteiros.")
            continue

        i = letra_para_indice(origem)
        j = letra_para_indice(destino)
        matriz[i][j] = peso
        matriz[j][i] = peso

        exibir_matriz(matriz, num_vertices)

# Consulta de caminho
origem = input("\nVértice de origem (ex: A): ").upper()
destino = input("Vértice de destino (ex: E): ").upper()

distancia, caminho = dijkstra(matriz, origem, destino, num_vertices)

print(f"\nMenor caminho de {origem} até {destino}:")
if distancia == float('inf'):
    print("Não há caminho.")
else:
    print(f"Menor distância: {distancia}")
    print(f"Caminho escolhido: {' → '.join(caminho)}")