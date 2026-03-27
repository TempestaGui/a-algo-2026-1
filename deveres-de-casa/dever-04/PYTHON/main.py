import math

"""
Metodo para calculo da função de forma recursiva 
"""

def f(n):
    if n == 1:
        return 2
    return 2 * f(n - 1) + math.pow(n, 2)


"""
Metodo para calculo da formula fechada
    Encontramos a formula fechada resolvendo a recorrencia. 
    F(n) = 2·F(n-1)


    F(n) = 7·2ⁿ - 2n² - 4n - 6
"""

def f_fechada(n):
    return 13 * int(math.pow(2, n-1)) - n**2 - 4*n - 6


n = int(input("Entre com o valor de n: "))
print(f"Recursão:  f({'{'}n{'}'}) = {f(n)}")
print(f"Fórmula fechada: f({'{'}n{'}'}) = {f_fechada(n)}")

"""
    Conclusão:
        A função recursiva tem complexidade O(n), pois realiza apenas
        uma chamada recursiva por nível até atingir o caso base.

        A fórmula fechada resolve em O(1), calculando o resultado
        diretamente sem recursão.
"""
