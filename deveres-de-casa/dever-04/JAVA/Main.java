package deveres_de_casa.dever_04.JAVA;
import java.util.*;

public class Main {

    public static int f(int n){
        if(n == 1){
            return 2;
        }
        return (int)(2 * f(n - 1) + Math.pow(n, 2));
    }

    public static int f_fechada(int n){
        return (int)(13 * Math.pow(2, n-1) - n*n - 4*n - 6);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Entre com n: ");
        int n = scanner.nextInt();

        System.out.println("Recursão:  f "+f(n));
        System.out.println("Recursão: f_fechada "+f_fechada(n));
    }
}