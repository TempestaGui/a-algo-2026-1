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