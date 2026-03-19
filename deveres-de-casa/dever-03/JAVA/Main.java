package deveres_de_casa.dever_03.JAVA;

import deveres_de_casa.dever_03.JAVA.service.PalindromoService;

public class Main {
    public static void main(String[] args) {
        /*
            Deve retornar ture
         */
        int[] numero = {1,2,3,2,1};
        System.out.println(PalindromoService.ehPalindromo(numero));

        /*
            Deve retornar false
         */
        numero = new int[]{1,2,3,3,3,1};
        System.out.println(PalindromoService.ehPalindromo(numero));
    }
}
