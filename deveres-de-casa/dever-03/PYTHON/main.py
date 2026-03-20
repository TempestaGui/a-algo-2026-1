def verificar_eh_palindromo(palavra, inicio, fim):
    """
        Verificar, se os indices forem iguais então é um palindromo
    """
    if inicio >= fim:
        return True

    """
        Verificar, se forem diferentes significa que a entrada não é um palindromo
    """
    if palavra[inicio] != palavra[fim]:
        return False
    
    """
        Realizar a chamada recursiva, passando novamente a palavra
        porem agora passamos o proximo indice do inicio e o descemos um do final
        e assim por diante ate ou retornar o true ou o false
    """
    return verificar_eh_palindromo(palavra, inicio + 1, fim - 1)



def main(): 
    """
        para chamar a verificacao, temos que mandar o array quer sera lido, a posicao inicial que devera comecar, 
        e a posicao final, utilizamos o - 1 pois o array começa em 0
        verificar_eh_palindromo(numero, 0, len(numero) - 1)
    """

    """
        Primeiro print deve retornar true
    """
    numero = [1,2,3,3,2,1]
    print(verificar_eh_palindromo(numero, 0, len(numero) - 1))

    """
        Segundo print deve retornar false
    """
    numero = [1,2,3,3,1,2]
    print(verificar_eh_palindromo(numero, 0, len(numero) - 1))

if __name__ == "__main__":
    main()