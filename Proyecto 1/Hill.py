es_entero = lambda x: (x).is_integer()
sqrt = lambda x: x**(1/2)

def creaMatriz(n, palabra):
    n_gramas = []
    lista = []
    i = 0
    for letra in palabra:
        lista.append(mapea_alfabeto(letra))
        i+=1
        if(i == n):
            n_gramas.append(lista)
            lista = []
            i = 0
    return n_gramas

def mapea_alfabeto(letra):
    i = 0
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    for l in alfabeto:
        if(l == letra):
            return i
        i+=1

def cifrar(clave, texto):
    """Cifra un texto usando el crifrado de Hill

    Devuelve el texto cifrado por el cifrado de Hill
    en mayusculas.

    :Parámetros:
    texto -- Texto que queremos crifrar
    clave -- clave con la que queremos crifrar

    Excepciones:
    
    
    """
    N = sqrt(len(clave))
    longitud_texto = len(texto)
    if(not es_entero(N)):
        print("No se puede formar una matriz con esa clave \n" )
        return
    if(not (longitud_texto % N) == 0):
        print("No se puede cifrar la pabra con esa clave \n")
        return
    n_gramas = creaMatriz(N, texto)
    K = creaMatriz(N, clave)
    return n_gramas





    

    
    
    
