import sys
import time
import os

def menu():
    print("---Bienvenido al triangulo de pascal---")
    time.sleep(1)
    print("Ingresa\n0-Salir\n1-Iniciar el programa")
    valor = int(input())

    if valor == 0:
        SystemExit()
    elif valor == 1:
        pascal()
    elif valor >= 2:
        print("Te crees gracioso? 7u7, pues dejame decirte que no UwU")
        return menu()

    


def pascal():
    listBase = [1,1]
    listDeList = [1]

    listDos = []

    print("-----Ejercicio de Pascal-----")
    print("Ingresa el valor limite para el triangulo: ")
    num = int(input())
    time.sleep(1)

    print(listDeList)
    print(listBase)
    for ciclo in range(2, num):
       for ciclo2 in range(0, ciclo):
           if ciclo2 == 0 or ciclo2 == ciclo - 1:
                listDos.append(1)
           if ciclo2 != (ciclo - 1):
               listDos.append(listBase[ciclo2] + listBase[ciclo2 + 1])
       print(listDos)        
       listBase = listDos.copy()
       listDos.clear()
            


    return menu()
menu()
