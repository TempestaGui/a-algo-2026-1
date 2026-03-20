package deveres_de_casa.dever_03.JAVA.service;

public class PalindromoService {

    public static boolean ehPalindromo(int[] palavra){
        return verificar(palavra, 0, palavra.length - 1);
    }

    public static boolean verificar(int[] palavra, int inicio, int fim){
        if(inicio >= fim){
            return true;
        }

        if(palavra[inicio] != palavra[fim]){
            return false;
        }
        return verificar(palavra, inicio + 1, fim - 1);
    }
}
