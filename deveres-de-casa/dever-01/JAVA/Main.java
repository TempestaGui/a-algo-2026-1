package deveres_de_casa.dever_01.JAVA;


import deveres_de_casa.dever_01.JAVA.service.GeracaoListaService;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        int[] tamanhos = {1000, 5000, 10000, 20000, 50000};
        int j;
        int aux;

        for(int n: tamanhos){
            List<Integer> listaOriginal = GeracaoListaService.gerarLista(n);
            List<Integer> listaInsertion = new ArrayList<>(listaOriginal);
            List<Integer> listaSort = new ArrayList<>(listaOriginal);

            /*
              INSERTION
            */
            long inicio = System.nanoTime();

         for(int i = 1; i< listaInsertion.size(); i++){
            aux = listaInsertion.get(i);
            j = i - 1;
            while(j >= 0 && listaInsertion.get(j) > aux){
                listaInsertion.set(j+1, listaInsertion.get(j));
                j--;
            }
             listaInsertion.set(j+1, aux);
         }
            long fim = System.nanoTime();

            long tempoExecucao = fim - inicio;
            System.out.println("Lista de tamanho(Insertion): "+ listaInsertion.size());
            System.out.println("Tempo de execução: "+tempoExecucao/ 1_000_000.0 + " ms");

            /*
              SORT
            */
            inicio = System.nanoTime();
            Collections.sort(listaSort);
            fim = System.nanoTime();

            tempoExecucao =  fim - inicio;

            System.out.println("Lista de tamanho(Sort): "+listaSort.size());
            System.out.println("Tempo execução sort: "+tempoExecucao/ 1_000_000.0 + " ms");
        }
    }
}