"""1. Agregar un libro: Permite al usuario añadir un nuevo libro, solicitando el título, el
autor, el año de publicación y el género del libro. El libro debe ser almacenado en
una lista como un diccionario.

2. Mostrar libros: Muestra todos los libros almacenados en la lista, incluyendo el
título, el autor, el año de publicación y el género de cada libro.

3. Buscar libro por título: Permite al usuario buscar un libro por su título y muestra
toda la información del libro encontrado.

4. Actualizar información del libro: Permite al usuario actualizar la información de un
libro existente, identificándolo por su título.

5. Guardar libros en un archivo JSON: Permite al usuario guardar todos los libros en
un archivo JSON cuyo nombre será especificado por el usuario.

6. Salir: Termina la ejecución del programa."""

import os, time
from funcion_b import *

while True:
    os.system('cls')
    print('\tMENÚ BIBLIOTECA')
    print('\nopc.1 = agregar un libro.')
    print('opc.2 = mostrar libros.')
    print('opc.3 = buscar libro.')
    print('opc.4 = actualizar info de un libro.')
    print('opc.5 = guardar libros en json.')
    print('opc.6 = salir.')

    opc = int(input('\nseleccióne una opción: '))
    os.system('cls')
    if opc==1:
        opc_1()
    elif opc==2:
        opc_2()
        time.sleep(4)
    elif opc==3:
        opc_3()
        time.sleep(3)
    elif opc==4:
        opc_4()
    elif opc==5:
        pass
    else:
        print('adios..')
        break