# Analise de complexidade de algoritmo 

## 1) Merge Sort
   > O algoritmo Merge Sort utiliza uma estrategia de divisão e conquista. Ou seja, o problema é dividido em duas partes iguais, sendo resolvido recursivamente e depois combinado

    A recorrência que descreve o tempo de execução é: 
   ```
     T(n) = 2T(n/2) + n

     - onde o termo (2T(n/2)) representa as duas chamadas recursivas
     - o termo (n) corresponde ao custo da etapa de intercalação (merge)
   ```
   > Aplicando o Teorema Mestre:

      * a = 2
      * b = 2
      * f(n) = n

    Calculando:

   ```
     {log_b(a)} = {log_2(2)} = 1
     f(n) = n = n^1
     f(n) = Θ(n^(log_b(a))) -> Caso 2
   ```

   Complexidade: Θ(n * log(n))

## 2) Multiplicação de Matrizes
   > Na multiplicação tradicional de matrizes quadradas de ordem (n), utilizam-se três laços aninhados.
   > Cada elemento da matriz resultado é calculado a partir de um somatório de (n) multiplicações, e isso é feito para todos os (n^2) elementos.

   A recorrencia que descreve o tempo de execução é:

   ```
    n * n * n = n^3
   ```
   Logo a complexidade do algoritmo é: Θ(n^3)

## 3) Resolução de Recorrências

   ### a) **T(n) = 2T(n/4) + √n**

     primeiro identificamos os parâmetros

      * a = 2
      * b = 4
      * f(n) = √n

     Calculando:

       log_b(a) = log_4(2) = 0,5
       f(n) =  √n = n^0,5
       f(n) = Θ(n^(log_b(a))) -> caso 2
       

       Complexidade: Θ(√n * log(n))

   ### b) **T(n) = 2T(n/4) + n**

      primeiro identificamos os parâmetros

      * a = 2
      * b = 4
      * f(n) = n

      Calculando:

       log_b(a) = log_4(2) = 0,5
       f(n) = n = n^1
       n^1 > n^0,5 ou seja -> caso 3

       Complexidade: Θ(n)

   ### c) **T(n) = 16T(n/4) + n^2**
   
     primeiro identificamos os parâmetros

     * a = 16
     * b = 4
     * f(n) = n^2
  
      Calculando:

       log_b(a) = log_4(16) = 2
       f(n) = n^2
     
       > Como as funções têm o mesmo crescimento, aplica-se o caso 2 do Teorema Mestre.

       Complexidade: Θ(n^2 * log(n))

## 4) Conclusão

   A análise mostra que diferentes estratégias algorítmicas levam a diferentes ordens de crescimento:

   > Merge Sort: Θ(n * log(n)).  
   > Multiplicação de matrizes: Θ(n^3).  
   > Recorrência (a): Θ(√n * log(n)).  
   > Recorrência (b): Θ(n).  
   > Recorrência (c): Θ(n^2 * log(n))












   
