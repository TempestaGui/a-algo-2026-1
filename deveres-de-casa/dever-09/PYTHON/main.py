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