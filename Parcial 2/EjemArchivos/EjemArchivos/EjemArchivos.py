import os

def menu():

    #Abrir un archivo en modo de lectura
    file = open("Texto.txt", 'r')

    #Leer las lineas del archivo e imprimirlas
    print(file.readline(), file.readline())
    file.read

    #Cerrar el read
    file.close()

    lineList = []

    #Abrir un archivo con sentencia with
    with open("Texto.txt", 'r') as cajita:

        #Leer las lineas con un for
        for line in cajita:
            print(line)
            lineList.append(line)
        print(lineList)

    #Abrir un archivo en modo lectura+

    #Crear un nuevo archivo nuevo

    #Abrir o crear un archivo en modo de escritura+

    #Abrir un archivo en modo append

menu()