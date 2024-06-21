libro=[]
libros=[]
import os, time
def opc_1():
    libro=[]
    print('\tAGREGAR LIBRO')
    n_libro = input('ingresa el nombre del libro el cual deseas agregar: ')
    a_publicacion = int(input('ingresa el año de publicación del libro: '))
    genero = input('ingresa el género del libro: ')
    libro = {'n_libro':n_libro,
              'a_publicacion':a_publicacion, 
              'genero':genero}
    libros.append(libro)
    print('libro agregado con éxito.')

def opc_2():
    print('\tLIBROS ACTUALES')

    if len(libros)==0:
        print('deberias agregar un libro antes de usar esta opción.')
    else:
        for x in libros:
            print('\nNOMBRE DEL LIBRO: ', {x['n_libro']})
            print('AÑO DE PUBLICACIÓN: ', {x['a_publicacion']})
            print('GENERO DEL LIBRO: ', {x['genero']})

def opc_3():
    if len(libros)==0:
        print('deberias agregar un libro antes de usar esta opción.')
    else:
        busca_libros = input('ingresa el nombre del libro a buscar:')
        for diccionario in libros:
            if diccionario["n_libro"]==busca_libros:
                print('NOMBRE:',diccionario["n_libro"])
                print('AÑO PUBLICACIÓN:',diccionario["a_publicacion"])
                print('GENERO:',diccionario["genero"])
                return busca_libros
            else:
                print('no hay semejanzas.')

def opc_4():
    if len(libros)==0:
        print('deberias agregar un libro antes de usar esta opción.')
    else:
        print('\tACTUALIZACIÓN DE LIBRO')
        print('\nopciones de modificación:')
        print('\n1-NOMBRE.')
        print('2-AÑO PUBLICACIÓN.')
        print('3-GENERO.')
        print('4-TODO.')
        cambio = int(input('\ningresa el número para el tipo de cambio: '))
        if cambio==1:
            busca_libros = input('ingresa el nombre del libro a buscar:')
            C_nombre_n = input('ingrese el nuevo nombre del libro: ')
            for diccionario2 in libros:
                clave = diccionario2["n_libro"]== busca_libros
                if clave in diccionario2:
                    del diccionario2[clave]
                    diccionario2({"n_libro":C_nombre_n})


        elif cambio==2:
            busca_libros2 = input('ingresa el nombre del libro a buscar:')
            C_publicacion_n = input('ingrese el nuevo año de publicación: ')
            for diccionario22 in libros:
                clave_a = diccionario22["n_libro"]== busca_libros2
                if clave_a in diccionario22:
                    diccionario22({"a_publicacion":C_publicacion_n})
        elif cambio==3:
            pass
        else:
            pass

