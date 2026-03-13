import time
import sys

"""
    Declaramos os valores que foi passado na questão para serem fatorados
"""

valores = [10, 100, 500, 1000]

"""
    Declarando um limite para que evite possiveis quebras do sistema
"""

sys.setrecursionlimit(2000)

"""
    Função para calcular o fatorial do numero de forma recursiva
"""

def processamento_numero(n): 
    """"
        Recebendo um argumento que sera o numero inteiro que sera fatorado

        depois fazemos uma leve verificação para que se o numero for 0 ou 1 a fatoração sera 1

        apois isso chamamos de forma recursiva o nosso metodo para realizar o calculo da fatoração
    """

    if n == 0 or n == 1:
        return 1
    
    return n * processamento_numero(n - 1)


""""
    Função para calcular o tempo levado para fatorar o numero 
"""

def tempo_levado(n): 
    """
        Iniciamos o time 
    """
    inicio = time.perf_counter()
    """
        Chamamos a funçao para realizar a fatoração
    """
    processamento_numero(n)

    """
        Encerramos o time e retornamos o resultado do tempo levado
    """
    fim = time.perf_counter()

    return fim - inicio


"""
    Função main para retornar os resultados
"""

def main():
    for n in valores: 
        tempo = tempo_levado(n)

        print("n = ", n)
        print("Tempo necessrio: ",  tempo * 1000, "ms")
        print()

if __name__ == "__main__":
    main()

"""
    Conclusão da atividade: 
        A implementação do algoritimo de calculo fatorial foi feita utilizando recursividade 
        para cada chamada dos valores de n o valor é reduzido em 1 ate atingir o caso da base ser de (n = 1)

        Sendo assim o numero das chamadas recursivas sempre sera proporcional ao valor de n. Por tanto, Esse algoritmo esta realizando n chamadas
        sendo então considerado um algoritmo de o(n). 

        o tempo de execução cresce linearmente ao tamanho da entrada do valor. 
"""