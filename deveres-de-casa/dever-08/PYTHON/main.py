## Código 1 — Dijkstra (com comentários)

# ============================================
# ALGORITMO DE DIJKSTRA
# ============================================
# Objetivo:
# Encontrar o menor caminho do nó 0 até o nó 4
#
# Grafo utilizado:
# (0,1)=4
# (0,2)=1
# (2,1)=2
# (1,3)=1
# (2,4)=5
# (3,4)=1
# ============================================

import heapq  # Biblioteca usada para fila de prioridade

# Representação do grafo usando lista de adjacência
# Cada vértice possui:
# (vizinho, peso_da_aresta)
grafo = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (4, 5)],
    3: [(4, 1)],
    4: []
}

# Função principal do algoritmo
def dijkstra(grafo, inicio):

    # Inicializa todas as distâncias com infinito
    distancias = {vertice: float('inf') for vertice in grafo}

    # Armazena o vértice anterior de cada nó
    predecessores = {vertice: None for vertice in grafo}

    # Distância do nó inicial até ele mesmo é 0
    distancias[inicio] = 0

    # Fila de prioridade:
    # (distância, vértice)
    fila = [(0, inicio)]

    # Controle das iterações
    iteracao = 1

    # Enquanto existir vértice na fila
    while fila:

        # Remove o vértice com menor distância
        distancia_atual, vertice_atual = heapq.heappop(fila)

        print(f"\n========== ITERAÇÃO {iteracao} ==========")
        print(f"Vértice visitado: {vertice_atual}")

        # Percorre os vizinhos do vértice atual
        for vizinho, peso in grafo[vertice_atual]:

            # Calcula a nova distância
            nova_distancia = distancia_atual + peso

            # Verifica se encontrou caminho menor
            if nova_distancia < distancias[vizinho]:

                # Atualiza a menor distância
                distancias[vizinho] = nova_distancia

                # Guarda o predecessor
                predecessores[vizinho] = vertice_atual

                # Adiciona na fila
                heapq.heappush(fila, (nova_distancia, vizinho))

        # Exibe tabela das distâncias atuais
        print("\nTabela Atual:")
        print("Vértice | Distância | Predecessor")

        for v in grafo:
            print(
                f"{v:^8} | "
                f"{distancias[v]:^10} | "
                f"{str(predecessores[v]):^12}"
            )

        iteracao += 1

    # Retorna resultados finais
    return distancias, predecessores


# ============================================
# EXECUÇÃO DO ALGORITMO
# ============================================

distancias, predecessores = dijkstra(grafo, 0)

# ============================================
# RECONSTRUÇÃO DO MENOR CAMINHO
# ============================================

destino = 4
caminho = []

# Volta pelos predecessores
while destino is not None:
    caminho.append(destino)
    destino = predecessores[destino]

# Inverte o caminho
caminho.reverse()

# ============================================
# RESULTADO FINAL
# ============================================

print("\n========== RESULTADO FINAL ==========")
print("Menor caminho encontrado:", caminho)
print("Custo mínimo:", distancias[4])

# Código 2 — Bellman-Ford (com comentários)

# ============================================
# ALGORITMO DE BELLMAN-FORD
# ============================================
# Objetivo:
# Calcular menores caminhos mesmo com pesos negativos
# e verificar se existe ciclo negativo.
#
# Grafo utilizado:
#
# 0 -> 1 (5)
# 1 -> 2 (1)
# 1 -> 3 (2)
# 2 -> 4 (1)
# 4 -> 3 (-1)
# ============================================

# Quantidade de vértices
vertices = 5

# Lista de arestas:
# (origem, destino, peso)
arestas = [
    (0, 1, 5),
    (1, 2, 1),
    (1, 3, 2),
    (2, 4, 1),
    (4, 3, -1)
]

# Função principal do algoritmo
def bellman_ford(vertices, arestas, origem):

    # Inicializa todas as distâncias com infinito
    distancias = [float('inf')] * vertices

    # Guarda o predecessor de cada vértice
    predecessores = [None] * vertices

    # Distância do nó inicial até ele mesmo é 0
    distancias[origem] = 0

    # ============================================
    # RELAXAMENTO DAS ARESTAS
    # Executa V-1 vezes
    # ============================================

    for i in range(vertices - 1):

        print(f"\n========== ITERAÇÃO {i + 1} ==========")

        # Percorre todas as arestas
        for u, v, peso in arestas:

            # Verifica se existe caminho menor
            if distancias[u] != float('inf') and distancias[u] + peso < distancias[v]:

                # Atualiza distância
                distancias[v] = distancias[u] + peso

                # Atualiza predecessor
                predecessores[v] = u

        # Exibe tabela atual
        print("Vértice | Distância | Predecessor")

        for v in range(vertices):
            print(
                f"{v:^8} | "
                f"{distancias[v]:^10} | "
                f"{str(predecessores[v]):^12}"
            )

    # ============================================
    # VERIFICAÇÃO DE CICLO NEGATIVO
    # ============================================

    ciclo_negativo = False

    # Se ainda conseguir relaxar uma aresta,
    # existe ciclo negativo
    for u, v, peso in arestas:

        if distancias[u] != float('inf') and distancias[u] + peso < distancias[v]:
            ciclo_negativo = True
            break

    # ============================================
    # RESULTADO FINAL
    # ============================================

    print("\n========== RESULTADO FINAL ==========")

    if ciclo_negativo:
        print("Existe ciclo negativo no grafo.")
    else:
        print("Não existe ciclo negativo no grafo.")

    # Exibe distâncias finais
    print("\nDistâncias finais:")

    for i in range(vertices):
        print(f"Vértice {i}: {distancias[i]}")

    return distancias, predecessores


# ============================================
# EXECUÇÃO DO ALGORITMO
# ============================================

bellman_ford(vertices, arestas, 0)
