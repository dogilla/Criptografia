es_entero = lambda x: (x).is_integer()
sqrt = lambda x: x**(1/2)

def creaMatriz(n, palabra):
    """
    crea una matriz de nxn que representa
    decimalmente la palabra que recibe.
    """
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
    """
    funcion que mapea un letra del alfabeto a su representacion
    decimal
    """
    i = 0
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    for l in alfabeto:
        if(l == letra):
            return i
        i+=1

def mapea_numero(numero):
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    return alfabeto[numero]


def multiplica_matrices(A, B):
    """
    funcion que multiplica dos matrices en forma de lista
    """
    resultado = []
    escalar = 0
    for lista in A:
        escalar = 0
        i = 0
        for elemento in lista:
            escalar += elemento*B[i]
            i += 1
        resultado.append(escalar)
    return resultado
        

def cifrar(clave, texto):
    """Cifra un texto usando el crifrado de Hill

    Devuelve el texto cifrado por el cifrado de Hill
    en mayusculas.

    :Parámetros:
    texto -- Texto que queremos crifrar
    clave -- clave con la que queremos crifrar

    Excepciones:
    
    
    """
    N = sqrt(len(clave)) #nº de columnas o filas de la matriz K
    longitud_texto = len(texto) 
    if(not es_entero(N)):
        print("No se puede formar una matriz con esa clave \n" )
        return
    if(not (longitud_texto % N) == 0):
        print("No se puede cifrar la pabra con esa clave \n")
        return
    n_gramas = creaMatriz(N, texto) #lista con los nºgramas
    K = creaMatriz(N, clave) #crea la matriz principal
    cifrado = []
    for n_grama in n_gramas:
        cifrado.append(multiplica_matrices(K, n_grama))
    cifrado = sum(cifrado, []) #unimos la lista en una sola
    cifrado = map(lambda x: mapea_numero(x % 27), cifrado)
    cifrado_final = ""
    for letra in list(cifrado):
        cifrado_final += letra

    return cifrado_final

def decifrar(clave, texto):
    return





    

    
    
    
