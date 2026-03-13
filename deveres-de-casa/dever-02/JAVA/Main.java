package deveres_de_casa.dever_02.JAVA;

import java.math.BigInteger;

public class Main{
    /*
        Função para calcular o fatorial do numero de forma recursiva
        Recebendo um argumento que sera o numero inteiro que sera fatorado
        depois fazemos uma leve verificação para que se o numero for 0 ou 1 a fatoração sera 1
        apois isso chamamos de forma recursiva o nosso metodo para realizar o calculo da fatoração
    */
    public static BigInteger processamentoNumero(int numero){
        if(numero == 0 || numero == 1){
            return BigInteger.ONE;
        }

        return processamentoNumero(numero - 1).multiply(BigInteger.valueOf(numero));
    }

    /*
        Função para calcular o tempo levado para fatorar o numero
        Iniciamos o time
        Chamamos a funçao para realizar a fatoração
        Encerramos o time e retornamos o resultado do tempo levado
    */
    public static long tempo(int n){
        long inicio;
        long fim;
        BigInteger resultado;

        inicio = System.nanoTime();
        resultado =  processamentoNumero(10);
        System.out.println("Resultado: "+resultado);
        fim = System.nanoTime();

        return fim - inicio;
    }

    /*
        Função main para retornar os resultados
    */
    public static void main(String[] args) {
        int[] value = {10, 100, 500, 1000};

        for(int n : value){
            System.out.println("n: "+ n);
            System.out.println("Tempo de execução: "+ tempo(n)/ 1_000_000.0 + " ms");
            System.out.println();
        }
    }

    /*
        Conclusão da atividade:
        A implementação do algoritimo de calculo fatorial foi feita utilizando recursividade
        para cada chamada dos valores de n o valor é reduzido em 1 ate atingir o caso da base ser de (n = 1)

        Sendo assim o numero das chamadas recursivas sempre sera proporcional ao valor de n. Por tanto, Esse algoritmo esta realizando n chamadas
        sendo então considerado um algoritmo de o(n).

        o tempo de execução cresce linearmente ao tamanho da entrada do valor.
    */
}