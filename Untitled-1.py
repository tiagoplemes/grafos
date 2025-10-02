def letra_para_indice(letra):
    return ord(letra.upper()) - ord('A')

def indice_para_letra(indice):
    return chr(indice + ord('A'))

def dijkstra_para_destino(matriz, origem, destino, num_vertices):
    distancias = [float('inf')] * num_vertices
    visitados = [False] * num_vertices
    predecessores = [None] * num_vertices

    origem_idx = letra_para_indice(origem)
    destino_idx = letra_para_indice(destino)
    distancias[origem_idx] = 0

    while True:
        # Encontra o vértice não visitado com menor distância
        min_dist = float('inf')
        u = -1
        for i in range(num_vertices):
            if not visitados[i] and distancias[i] < min_dist:
                min_dist = distancias[i]
                u = i

        if u == -1 or u == destino_idx:
            break  # Parou porque não há mais vértices ou chegou ao destino

        visitados[u] = True

        # Atualiza distâncias dos vizinhos
        for v in range(num_vertices):
            if matriz[u][v] > 0 and not visitados[v]:
                nova_dist = distancias[u] + matriz[u][v]
                if nova_dist < distancias[v]:
                    distancias[v] = nova_dist
                    predecessores[v] = u

    return distancias[destino_idx], reconstruir_caminho(predecessores, destino_idx)

def reconstruir_caminho(predecessores, destino_idx):
    caminho = []
    atual = destino_idx
    while atual is not None:
        caminho.insert(0, indice_para_letra(atual))
        atual = predecessores[atual]
    return caminho

# Entrada do usuário
while True:
    try:
        num_vertices = int(input("Quantidade de vértices (máx 26): "))
        if 1 <= num_vertices <= 26:
            break
        else:
            print("⚠️ Número inválido. Digite um valor entre 1 e 26.")
    except ValueError:
        print("⚠️ Entrada inválida. Digite um número inteiro.")

matriz = [[0] * num_vertices for _ in range(num_vertices)]
for i in range(num_vertices):
    matriz[i][i] = 0  # Zera a diagonal principal

print("Digite as arestas no formato: origem destino peso (ex: A B 5). Digite 'fim' para encerrar.")
while True:
    entrada = input("Aresta: ")
    if entrada.lower() == 'fim':
        break

    # ⬇️ Esse bloco precisa estar DENTRO do while
    partes = entrada.strip().split()
    if len(partes) != 3:
        print("⚠️ Formato inválido. Use: origem destino peso (ex: A B 4)")
        continue

    origem, destino, peso = partes
    origem = origem.upper()
    destino = destino.upper()

    vertices_validos = [indice_para_letra(i) for i in range(num_vertices)]
    if origem not in vertices_validos or destino not in vertices_validos:
        print(f"⚠️ Vértices devem estar entre: {', '.join(vertices_validos)}")
        continue

    if origem == destino:
        print("⚠️ Arestas na diagonal (ex: A A) não são permitidas.")
        continue

    try:
        peso = int(peso)
        if peso < 0:
            print("⚠️ Peso não pode ser negativo.")
            continue
    except ValueError:
        print("⚠️ Peso inválido. Use um número inteiro.")
        continue

    i = letra_para_indice(origem)
    j = letra_para_indice(destino)
    matriz[i][j] = peso
# Para grafo não direcionado, também:
# matriz[j][i] = peso

origem = input("\nVértice de origem (ex: A): ").upper()
destino = input("Vértice de destino (ex: E): ").upper()

distancia, caminho = dijkstra_para_destino(matriz, origem, destino, num_vertices)

print(f"\nMenor caminho de {origem} até {destino}:")
if distancia == float('inf'):
    print("Sem caminho possível.")
else:
    print(f"Distância: {distancia}")
    print(f"Caminho: {' → '.join(caminho)}")