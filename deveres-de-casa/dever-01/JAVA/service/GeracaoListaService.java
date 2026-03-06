package deveres_de_casa.dever_01.JAVA.service;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class GeracaoListaService {

    public static List<Integer> gerarLista(int n) {
        Random random = new Random();
        List<Integer> lista = new ArrayList<>();

        for(int i = 0; i < n; i++){
            lista.add(random.nextInt(42)); //Gerar numeros aleatorios
        }
        return lista;
    }
}

