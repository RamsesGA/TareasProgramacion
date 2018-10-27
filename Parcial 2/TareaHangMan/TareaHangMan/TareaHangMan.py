#Text Formatting para poder hacer el monito del Hang Man
import sys
import os
import time
import random

def menu():
    print("Bienvenido al juego del ahorcado")
    print("Selecciona\n 0-Para salir\n 1-Para iniciar")
    valor = int(input())

    if valor == 0:
        SystemExit()
    elif valor == 1:
        ahorcado()

def comp(listaPalabra:list, listaLetras:list):
	inst = 0
	for ciclo in range(0, len(listaLetras)):
		for ciclo2 in range(0, len(listaPalabra) -1):
			if listaLetras[ciclo] == listaPalabra[ciclo2]:
				inst = inst + 1
	if inst == (len(listaPalabra)-1):
		print("Ganaste, la palabra era: ", listaPalabra)
		return 1

def ahorcado():
    cajaList = []
    lineas = []
    listLetra = []
    final = 0
    vidas = 5
    
    print("Bienvenido a continuación definiremos la palabra para que adivines...")
    time.sleep(1)

    cajita = open("Palabras.txt", 'r').readlines()
    cajaList = random.choice(cajita)    

    print("Palabra: ", cajaList) #QUITAR
    print("Numero de letras: ", len(cajaList)-1) #QUITAR

    
    while vidas > 0:
        print("Tu numero de vidas: ", vidas)
        print("Ingresa la palabra en MAYUSCULAS:")
        letra = input()
        letra = letra.upper()
        if letra not in listLetra:		
            if letra not in cajaList:
                print("1 vida menos")
                listLetra.append(letra)
                vidas = vidas - 1
            else:
                listLetra.append(letra)
                print("Sigue adelante")
        else:
            print("Palabra ya ingreseda, introduzca otra")
        if comp(cajaList, listLetra) == 1:
            break
        if vidas == 0:
            print("--------FIN DEL JUEGO--------")
            break

            


    return menu()

menu()
