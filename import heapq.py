import heapq

def dijkstra(matriz, inicio):
    n = len(matriz)  # número de vértices
    distancias = [float('inf')] * n
    distancias[inicio] = 0
    fila = [(0, inicio)]
    
    while fila:
        distancia_atual, no_atual = heapq.heappop(fila)
        
        if distancia_atual > distancias[no_atual]:
            continue
        
        for vizinho in range(n):
            peso = matriz[no_atual][vizinho]
            if peso > 0:  # existe aresta
                nova_dist = distancia_atual + peso
                if nova_dist < distancias[vizinho]:
                    distancias[vizinho] = nova_dist
                    heapq.heappush(fila, (nova_dist, vizinho))
    
    return distancias


# ---- Programa principal ----
n = int(input("Digite a quantidade de vértices: "))

print("\nDigite a matriz de adjacência (valores 0 = sem ligação):")
matriz = []
for i in range(n):
    linha = list(map(int, input(f"Linha {i+1}: ").split()))
    matriz.append(linha)

inicio = int(input(f"\nEscolha o vértice inicial (0 até {n-1}): "))

distancias = dijkstra(matriz, inicio)

print("\nMenores distâncias a partir do vértice", inicio)
for i, d in enumerate(distancias):
    print(f"{inicio} -> {i} = {d}")