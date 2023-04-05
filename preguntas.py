"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
from collections import Counter

print("Hecho por Juan Pablo Buitrago Diaz CC 1000.206.552")
datos = open('data.csv','r').readlines()
datos = [y.replace("\n","") for y in datos]  
datos = [y.split("\t") for y in datos]

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    return sum([int(x[1]) for x in datos])

#print(pregunta_01())

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    return sorted(Counter([str(x[0]) for x in datos]).most_common(5), key=lambda tupla: tupla[0])

#print(pregunta_02())

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    suma = {} 
    for letra, numero in list(zip([x[0] for x in datos],[x[1] for x in datos])):
        suma[letra] = suma.get(letra,0) + int(numero)
    lista = sorted([(key,value) for key,value in suma.items()],key=lambda tupla: tupla)

    return lista

#print(pregunta_03())

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    ocurrencias = [y[1] for y in [y.split('-') for y in [y[2] for y in datos]]]
    contador = Counter(ocurrencias).most_common()

    return sorted(contador)

#print(pregunta_04())

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    columnas = [(y[0],y[1]) for y in datos]
    lista = []
    for tupla in columnas:
        if(tupla[0] not in [y[0] for y in lista]):
            letra = tupla[0]
            maximo = max([int(y[1]) for y in columnas if y[0] == letra])
            minimo = min([int(y[1]) for y in columnas if y[0] == letra])
            lista.append((letra,maximo,minimo))

    return sorted(lista)

#print(pregunta_05())

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    diccionario = []
    for i in [y[4].split(",") for y in datos]:
        for j in i:
            diccionario.append(j)
    diccionario = [y.split(":") for y in diccionario]

    respuesta = []
    for tupla in diccionario:
        if tupla[0] not in [y[0] for y in respuesta]:
            clave = tupla[0]
            minimo = min([int(y[1]) for y in diccionario if y[0] == clave])
            maximo = max([int(y[1]) for y in diccionario if y[0] == clave])
            respuesta.append((clave,minimo,maximo))

    return sorted(respuesta)

#print(pregunta_06())

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    columnas = [(y[1],y[0]) for y in datos]
    lista = []
    for tupla in columnas:
        if int(tupla[0]) not in [int(y[0]) for y in lista]:
            numero = int(tupla[0])
            letras = [letra for letra in [y[1] for y in columnas if int(y[0]) == numero]]
            lista.append((numero,letras))

    return sorted(lista)

#print(pregunta_07())

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    columnas = [(y[1],y[0]) for y in datos]
    lista = []
    for tupla in columnas:
        if int(tupla[0]) not in [int(y[0]) for y in lista]:
            numero = int(tupla[0])
            letras = [letra for letra in [y[1] for y in columnas if int(y[0]) == numero]]
            letras = sorted(list(set(letras)))

            lista.append((numero,letras))

    return sorted(lista)

#print(pregunta_08())

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    diccionario = []
    for i in [y[4].split(",") for y in datos]:
        for j in i:
            diccionario.append(j)
    diccionario = sorted([y.split(":") for y in diccionario])
    dic = {}
    for tupla in diccionario:
        dic[tupla[0]] = dic.get(tupla[0],0) + 1

    return dic

#print(pregunta_09())

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]

    """
    
    return


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
