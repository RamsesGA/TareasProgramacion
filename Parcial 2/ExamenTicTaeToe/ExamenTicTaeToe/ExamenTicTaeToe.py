import sys
import time
import os
import random
import numpy

def menu():
    print("---Bienvenido al menu ingresa---\n0-Para salir\n1-Para iniciar PvP\n2-Para iniciar P vs IA")

    valor2 = str(input())
    if valor2.isnumeric() == True:
        valor = int(valor2)
        caja = open("Frases.txt", 'r').readlines()
        listCaja = random.choice(caja)

        if valor == 0:
            SystemExit()
        elif valor == 1:
            pvp()
        elif valor == 2:
            ia()
        elif valor >=3:
            print(listCaja)
            return menu()
    else:
        print("E R R O R")
        return menu()


def pvp():

    dibujo = [0, 0, 0]
    listDibujo = []
    listFinal = []
    F1 = []
    F2 = []
    intentos = 0

    print("---Player vs Player---")

    for ciclo in range(len(dibujo)):
        listDibujo.extend(dibujo)

    print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
    print("---------")
    print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
    print("---------")
    print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8])     

    while intentos <=3:
        j1 = []
        print("Jugador 1 ingresa un vector del 0 al 8: ")
        buu = str(input())
        if buu.isnumeric() == False:
            print("E R R O R")
            return pvp()
        else:
            j1 = buu
            intentos = intentos + 1 
            listFinal.extend(listDibujo)
            if j1[0] == '0': 
                if listFinal[0] == 'X' or listFinal[0] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    print("Valor usado, perdiste turno")
            if j1[0] == '0' and listFinal[0] == 0:
                listDibujo[0] = 'X'
                F1 = 'X'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8])          
            
            if j1[0] == '1': 
                if listFinal[1] == 'X' or listFinal[1] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    print("Valor usado, perdiste turno")
            if j1[0] == '1' and listFinal[1] == 0:
                listDibujo[1] = 'X'
                F1 = 'X'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
            
            if j1[0] == '2': 
                if listFinal[2] == 'X' or listFinal[2] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    print("Valor usado, perdiste turno")
            if j1[0] == '2' and listFinal[2] == 0:
                listDibujo[2] = 'X'
                F1 = 'X'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
                        
            if j1[0] == '3': 
                if listFinal[3] == 'X' or listFinal[3] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    print("Valor usado, perdiste turno")
            if j1[0] == '3' and listFinal[3] == 0:
                listDibujo[3] = 'X'
                F1 = 'X'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
            
            if j1[0] == '4': 
                if listFinal[4] == 'X' or listFinal[4] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    print("Valor usado, perdiste turno")
            if j1[0] == '4' and listFinal[4] == 0:
                listDibujo[4] = 'X'
                F1 = 'X'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
            
            if j1[0] == '5': 
                if listFinal[5] == 'X' or listFinal[5] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    print("Valor usado, perdiste turno")
            if j1[0] == '5' and listFinal[5] == 0:
                listDibujo[5] = 'X'
                F1 = 'X'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
            
            if j1[0] == '6': 
                if listFinal[6] == 'X' or listFinal[6] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    print("Valor usado, perdiste turno")
            if j1[0] == '6' and listFinal[6] == 0:
                listDibujo[6] = 'X'
                F1 = 'X'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
            
            if j1[0] == '7': 
                if listFinal[7] == 'X' or listFinal[7] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    print("Valor usado, perdiste turno")
            if j1[0] == '7' and listFinal[7] == 0:
                listDibujo[7] = 'X'
                F1 = 'X'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
            
            if j1[0] == '8': 
                if listFinal[8] == 'X' or listFinal[8] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    print("Valor usado, perdiste turno")
            if j1[0] == '8' and listFinal[8] == 0:
                listDibujo[8] = 'X'
                F1 = 'X'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
            
        buu2 = str(input("Jugador 2 ingresa un vector del 0 al 8:\n"))
        if buu2.isnumeric() == False:
                print("E R R O R")
                return pvp()
        else:
                #J U G A D O R 2
            j2 = buu2
            if j2[0] == '0': 
                if listFinal[0] == 'X' or listFinal[0] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    print("Valor usado, perdiste turno")
            if j2[0] == '0' and listFinal[0] == 0:
                listDibujo[0] = 'Z'
                F2 = 'Z'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
            
            if j2[0] == '1':
                if listFinal[1] == 'X' or listFinal[1] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    print("Valor usado, perdiste turno")
            if j2[0] == '1' and listFinal[1] == 0:
                listDibujo[1] = 'Z'
                F2 = 'Z'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
            
            if j2[0] == '2': 
                if listFinal[2] == 'X' or listFinal[2] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    print("Valor usado, perdiste turno")
            if j2[0] == '2' and listFinal[2] == 0:
                listDibujo[2] = 'Z'
                F2 = 'Z'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
            
            if j2[0] == '3': 
                if listFinal[3] == 'X' or listFinal[3] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    print("Valor usado, perdiste turno")
            if j2[0] == '3' and listFinal[3] == 0:
                listDibujo[3] = 'Z'
                F2 = 'Z'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
            
            if j2[0] == '4': 
                if listFinal[4] == 'X' or listFinal[4] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    print("Valor usado, perdiste turno")
            if j2[0] == '4' and listFinal[4] == 0:
                listDibujo[4] = 'Z'
                F2 = 'Z'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
            
            if j2[0] == '5': 
                if listFinal[5] == 'X' or listFinal[5] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    print("Valor usado, perdiste turno")
            if j2[0] == '5' and listFinal[5] == 0:
                listDibujo[5] = 'Z'
                F2 = 'Z'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
           
            if j2[0] == '6': 
                if listFinal[6] == 'X' or listFinal[6] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    print("Valor usado, perdiste turno")
            if j2[0] == '6' and listFinal[6] == 0:
                listDibujo[6] = 'Z'
                F2 = 'Z'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
            
            if j2[0] == '7': 
                if listFinal[7] == 'X' or listFinal[7] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    print("Valor usado, perdiste turno")
            if j2[0] == '7' and listFinal[7] == 0:
                listDibujo[7] = 'Z'
                F2 = 'Z'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
            
            if j2[0] == '8': 
                if listFinal[8] == 'X' or listFinal[8] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    print("Valor usado, perdiste turno")
            if j2[0] == '8' and listFinal[8] == 0:
                listDibujo[8] = 'Z'
                F2 = 'Z'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 

    #---W I N -- J U G A D O R ---
        
            if F1 == listDibujo[0] and F1 == listDibujo[1] and F1 == listDibujo[2]:
                    print("------Jugador 1, gano uvu------")
                    break
            elif F2 == listDibujo[0] and F2 == listDibujo[1] and F2 == listDibujo[2]:
                    print("------Jugador 2, gano uvu------")
                    break
            

        
            if F1 == listDibujo[3] and F1 == listDibujo[4] and F1 == listDibujo[5]:
                    print("------Jugador 1, gano uvu------")
                    break
            elif F2 == listDibujo[3] and F2 == listDibujo[4] and F2 == listDibujo[5]:
                    print("------Jugador 2, gano uvu------")
                    break
            

        
            if F1 == listDibujo[6] and F1 == listDibujo[7] and F1== listDibujo[8]:
                    print("------Jugador 1, gano uvu------")
                    break
            elif F2 == listDibujo[6] and F2 == listDibujo[7] and F2 == listDibujo[8]:
                    print("------Jugador 2, gano uvu------")
                    break
            

        # C O L U M N A S
        
            if F1 == listDibujo[0] and F1 == listDibujo[3] and F1 == listDibujo[6]:
                    print("------Jugador 1, gano uvu------")
                    break
            elif F2 == listDibujo[0] and F2 == listDibujo[3] and F2 == listDibujo[6]:
                    print("------Jugador 2, gano uvu------")
                    break
            

        
            if F1 == listDibujo[1] and F1 == listDibujo[4] and F1 == listDibujo[7]:
                    print("------Jugador 1, gano uvu------")
                    break
            elif F2 == listDibujo[1] and F2 == listDibujo[4] and F2 == listDibujo[7]:
                    print("------Jugador 2, gano uvu------")
                    break
            

        
            if F1 == listDibujo[2] and F1 == listDibujo[5] and F1 == listDibujo[8]:
                    print("------Jugador 1, gano uvu------")
                    break
            elif F2 == listDibujo[2] and F2 == listDibujo[5] and F2 == listDibujo[8]:
                    print("------Jugador 2, gano uvu------")
                    break
            

        # D I A G O N A L
        
            if F1 == listDibujo[0] and F1 == listDibujo[4] and F1 == listDibujo[8]:
                    print("------Jugador 1, gano uvu------")
                    break
            elif F2 == listDibujo[0] and F2 == listDibujo[4] and F2 == listDibujo[8]:
                    print("------Jugador 2, gano uvu------")
                    break
            

        
            if F1 == listDibujo[2] and F1 == listDibujo[4] and F1 == listDibujo[6]:
                    print("------Jugador 1, gano uvu------")
                    break
            elif F2 == listDibujo[2] and F2 == listDibujo[4] and F2 == listDibujo[6]:
                    print("------Jugador 2, gano uvu------")
                    break
            

    
    if intentos >= 4:
        if listDibujo[0] == 0:
            listDibujo[0] = 'X'
            print("----------F I N---------")
            print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
            print("---------")
            print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
            print("---------")
            print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8])
            print("E M P A T E")

        elif listDibujo[1] == 0:
            listDibujo[1] = 'X'
            print("----------F I N---------")
            print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
            print("---------")
            print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
            print("---------")
            print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8])
            print("E M P A T E")

        elif listDibujo[2] == 0:
            listDibujo[2] = 'X'
            print("----------F I N---------")
            print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
            print("---------")
            print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
            print("---------")
            print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8])
            print("E M P A T E")

        elif listDibujo[3] == 0:
            listDibujo[3] = 'X'
            print("----------F I N---------")
            print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
            print("---------")
            print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
            print("---------")
            print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8])
            print("E M P A T E")

        elif listDibujo[4] == 0:
            listDibujo[4] = 'X'
            print("----------F I N---------")
            print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
            print("---------")
            print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
            print("---------")
            print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8])
            print("E M P A T E")

        elif listDibujo[5] == 0:
            listDibujo[5] = 'X'
            print("----------F I N---------")
            print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
            print("---------")
            print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
            print("---------")
            print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8])
            print("E M P A T E")

        elif listDibujo[6] == 0:
            listDibujo[6] = 'X'
            print("----------F I N---------")
            print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
            print("---------")
            print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
            print("---------")
            print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8])
            print("E M P A T E")

        elif listDibujo[7] == 0:
            listDibujo[7] = 'X'
            print("----------F I N---------")
            print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
            print("---------")
            print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
            print("---------")
            print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8])       
            print("E M P A T E")

        elif listDibujo[8] == 0:
            listDibujo[8] = 'X'
            print("----------F I N---------")
            print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
            print("---------")
            print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
            print("---------")
            print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8])
            print("E M P A T E")

 
                #PARA REINICIAR EL PROGRAMA
    if intentos >= 3:
        print("Quieres volver a jugar?\n0-continuar\n1-Salir\n")
        final = int(input())
        if final == 0:
           return pvp()
        elif final == 1:
             SystemExit()
        elif final >=2:
             caja = open("Frases.txt", 'r').readlines()
             listCaja = random.choice(caja)
             print(listCaja)
             return menu()

 

def ia():
    dibujo = [0, 0, 0]
    listDibujo = []
    listFinal = []
    F1 = []
    F2 = []
    cajaDibujo = 0
    intentos = 0

    print("---Player vs IA---")

    for ciclo in range(len(dibujo)):
        listDibujo.extend(dibujo)

    print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
    print("---------")
    print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
    print("---------")
    print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8])
    
    caja = [0,1,2,3,4,5,6,7,8]
    while intentos <=3:
        j1 = []
        print(" Jugador 1 ingresa un vector del 0 al 8: ")
        buu = str(input())
        if buu.isnumeric() == False:
            print("E R R O R")
        else:
            j1 = buu
            intentos = intentos + 1 
            listFinal.extend(listDibujo)   
            if j1[0] == '0': 
                if listFinal[0] == 'X' or listFinal[0] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    print("Valor usado, perdiste turno")
            if j1[0] == '0' and listFinal[0] == 0:
                listDibujo[0] = 'X'
                caja.remove(0)
                F1 = 'X'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8])         
            
            if j1[0] == '1': 
                if listFinal[1] == 'X' or listFinal[1] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    print("Valor usado, perdiste turno")
            if j1[0] == '1' and listFinal[1] == 0:
                listDibujo[1] = 'X'
                caja.remove(1)
                F1 = 'X'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
            
            if j1[0] == '2': 
                if listFinal[2] == 'X' or listFinal[2] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    print("Valor usado, perdiste turno")
            if j1[0] == '2' and listFinal[2] == 0:
                listDibujo[2] = 'X'
                caja.remove(2)
                F1 = 'X'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
                        
            if j1[0] == '3': 
                if listFinal[3] == 'X' or listFinal[3] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    print("Valor usado, perdiste turno")
            if j1[0] == '3' and listFinal[3] == 0:
                listDibujo[3] = 'X'
                caja.remove(3)
                F1 = 'X'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
            
            if j1[0] == '4': 
                if listFinal[4] == 'X' or listFinal[4] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    print("Valor usado, perdiste turno")
            if j1[0] == '4' and listFinal[4] == 0:
                listDibujo[4] = 'X'
                caja.remove(4)
                F1 = 'X'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
            
            if j1[0] == '5': 
                if listFinal[5] == 'X' or listFinal[5] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    print("Valor usado, perdiste turno")
            if j1[0] == '5' and listFinal[5] == 0:
                listDibujo[5] = 'X'
                caja.remove(5)
                F1 = 'X'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
            
            if j1[0] == '6': 
                if listFinal[6] == 'X' or listFinal[6] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    print("Valor usado, perdiste turno")
            if j1[0] == '6' and listFinal[6] == 0:
                listDibujo[6] = 'X'
                caja.remove(6)
                F1 = 'X'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
            
            if j1[0] == '7': 
                if listFinal[7] == 'X' or listFinal[7] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    print("Valor usado, perdiste turno")
            if j1[0] == '7' and listFinal[7] == 0:
                listDibujo[7] = 'X'
                caja.remove(7)
                F1 = 'X'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
            
            if j1[0] == '8': 
                if listFinal[8] == 'X' or listFinal[8] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    print("Valor usado, perdiste turno")
            if j1[0] == '8' and listFinal[8] == 0:
                listDibujo[8] = 'X'          
                caja.remove(8)
                F1 = 'X'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 

            print("-----Turno de la IA-----")
           
            # P C
            cajita = 0
            listIa = []
            cajita = random.choice(caja)
            listIa.extend([cajita])
            print("Mi numero es: ",listIa)

            if listIa[0] == 0: 
                if listFinal[0] == 'X' or listFinal[0] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    caja.remove(0)
                    print("Valor usado, perdiste turno")
            if listIa[0] == 0 and listFinal[0] == 0:
                listDibujo[0] = 'Z'
                caja.remove(0)
                F2 = 'Z'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
            
            if listIa[0] == 1:
                if listFinal[1] == 'X' or listFinal[1] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    caja.remove(1)
                    print("Valor usado, perdiste turno")
            if listIa[0] == 1 and listFinal[1] == 0:
                listDibujo[1] = 'Z'
                caja.remove(1)
                F2 = 'Z'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
            
            if listIa[0] == 2: 
                if listFinal[2] == 'X' or listFinal[2] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    caja.remove(2)
                    print("Valor usado, perdiste turno")
            if listIa[0] == 2 and listFinal[2] == 0:
                listDibujo[2] = 'Z'
                caja.remove(2)
                F2 = 'Z'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
            
            if listIa[0] == 3: 
                if listFinal[3] == 'X' or listFinal[3] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    caja.remove(3)
                    print("Valor usado, perdiste turno")
            if listIa[0] == 3 and listFinal[3] == 0:
                listDibujo[3] = 'Z'
                caja.remove(3)
                F2 = 'Z'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
            
            if listIa[0] == 4: 
                if listFinal[4] == 'X' or listFinal[4] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    caja.remove(4)
                    print("Valor usado, perdiste turno")
            if listIa[0] == 4 and listFinal[4] == 0:
                listDibujo[4] = 'Z'
                caja.remove(4)
                F2 = 'Z'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
            
            if listIa[0] == 5: 
                if listFinal[5] == 'X' or listFinal[5] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    caja.remove(5)
                    print("Valor usado, perdiste turno")
            if listIa[0] == 5 and listFinal[5] == 0:
                listDibujo[5] = 'Z'
                caja.remove(5)
                F2 = 'Z'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
           
            if listIa[0] == 6: 
                if listFinal[6] == 'X' or listFinal[6] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    caja.remove(6)
                    print("Valor usado, perdiste turno")
            if listIa[0] == 6 and listFinal[6] == 0:
                listDibujo[6] = 'Z'
                caja.remove(6)
                F2 = 'Z'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
            
            if listIa[0] == 7: 
                if listFinal[7] == 'X' or listFinal[7] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    caja.remove(7)
                    print("Valor usado, perdiste turno")
            if listIa[0] == 7 and listFinal[7] == 0:
                listDibujo[7] = 'Z'
                caja.remove(7)
                F2 = 'Z'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 
            
            if listIa[0] == 8:
                if listFinal[8] == 'X' or listFinal[8] == 'Z':
                    intentos = intentos - 1
                    listFinal = listDibujo
                    caja.remove(8)
                    print("Valor usado, perdiste turno")
            if listIa[0] == 8 and listFinal[8] == 0:
                listDibujo[8] = 'Z'
                caja.remove(8)
                F2 = 'Z'
                listFinal = []
                listFinal.extend(listDibujo)
                print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
                print("---------")
                print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
                print("---------")
                print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8]) 

 
    #---W I N -- J U G A D O R ---
            
            if F1 == listDibujo[0] and F1 == listDibujo[1] and F1 == listDibujo[2]:
                 print("------Jugador 1, gano uvu------")
                 break
            elif F2 == listDibujo[0] and F2 == listDibujo[1] and F2 == listDibujo[2]:
                 print("------PC, gano uwu------")
                 break

            
            if F1 == listDibujo[3] and F1 == listDibujo[4] and F1 == listDibujo[5]:
                    print("------Jugador 1, gano uvu------")
                    break
            elif F2 == listDibujo[3] and F2 == listDibujo[4] and F2 == listDibujo[5]:
                    print("------PC, gano uwu------")
                    break


            
            if F1 == listDibujo[6] and F1 == listDibujo[7] and F1 == listDibujo[8]:
                    print("------Jugador 1, gano uvu------")
                    break
            elif F2 == listDibujo[6] and F2 == listDibujo[7] and F2 == listDibujo[8]:
                    print("------PC, gano uwu------")
                    break


        # C O L U M N A S
            
            if F1 == listDibujo[0] and F1 == listDibujo[3] and F1 == listDibujo[6]:
                    print("------Jugador 1, gano uvu------")
                    break
            elif F2 == listDibujo[0] and F2 == listDibujo[3] and F2 == listDibujo[6]:
                    print("------PC, gano uwu------")
                    break


           
            if F1 == listDibujo[1] and F1 == listDibujo[4] and F1 == listDibujo[7]:
                    print("------Jugador 1, gano uvu------")
                    break
            elif F2 == listDibujo[1] and F2 == listDibujo[4] and F2 == listDibujo[7]:
                    print("------PC, gano uwu------")
                    break


           
            if F1 == listDibujo[2] and F1 == listDibujo[5] and F1 == listDibujo[8]:
                    print("------Jugador 1, gano uvu------")
                    break
            elif F2 == listDibujo[2] and F2 == listDibujo[5] and F2 == listDibujo[8]:
                    print("------PC, gano uwu------")
                    break


        # D I A G O N A L
            
            if F1 == listDibujo[0] and F1 == listDibujo[4] and F1== listDibujo[8]:
                    print("------Jugador 1, gano uvu------")
                    break
            elif F2 == listDibujo[0] and F2 == listDibujo[4] and F2 == listDibujo[8]:
                    print("------PC, gano uwu------")
                    break


            
            if F1 == listDibujo[2] and F1 == listDibujo[4] and F1 == listDibujo[6]:
                    print("------Jugador 1, gano uvu------")
                    break
            elif F2 == listDibujo[2] and F2 == listDibujo[4] and F2 == listDibujo[6]:
                    print("------PC, gano uwu------")
                    break

    if intentos >= 4:
        if listDibujo[0] == 0:
            listDibujo[0] = 'X'
            print("----------F I N---------")
            print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
            print("---------")
            print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
            print("---------")
            print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8])
            print("E M P A T E")

        elif listDibujo[1] == 0:
            listDibujo[1] = 'X'
            print("----------F I N---------")
            print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
            print("---------")
            print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
            print("---------")
            print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8])
            print("E M P A T E")

        elif listDibujo[2] == 0:
            listDibujo[2] = 'X'
            print("----------F I N---------")
            print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
            print("---------")
            print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
            print("---------")
            print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8])
            print("E M P A T E")

        elif listDibujo[3] == 0:
            listDibujo[3] = 'X'
            print("----------F I N---------")
            print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
            print("---------")
            print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
            print("---------")
            print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8])
            print("E M P A T E")

        elif listDibujo[4] == 0:
            listDibujo[4] = 'X'
            print("----------F I N---------")
            print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
            print("---------")
            print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
            print("---------")
            print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8])
            print("E M P A T E")

        elif listDibujo[5] == 0:
            listDibujo[5] = 'X'
            print("----------F I N---------")
            print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
            print("---------")
            print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
            print("---------")
            print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8])
            print("E M P A T E")

        elif listDibujo[6] == 0:
            listDibujo[6] = 'X'
            print("----------F I N---------")
            print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
            print("---------")
            print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
            print("---------")
            print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8])
            print("E M P A T E")

        elif listDibujo[7] == 0:
            listDibujo[7] = 'X'
            print("----------F I N---------")
            print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
            print("---------")
            print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
            print("---------")
            print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8])       
            print("E M P A T E")

        elif listDibujo[8] == 0:
            listDibujo[8] = 'X'
            print("----------F I N---------")
            print(listDibujo[0],"|", listDibujo[1],"|", listDibujo[2])
            print("---------")
            print(listDibujo[3],"|", listDibujo[4],"|", listDibujo[5])
            print("---------")
            print(listDibujo[6],"|", listDibujo[7],"|", listDibujo[8])
            print("E M P A T E")

 
                #PARA REINICIAR EL PROGRAMA
    if intentos >= 3:
        print("Quieres volver a jugar?\n0-continuar\n1-Salir\n")
        final = int(input())
        if final == 0:
           return pvp()
        elif final == 1:
             SystemExit()
        elif final >=2:
             caja = open("Frases.txt", 'r').readlines()
             listCaja = random.choice(caja)
             print(listCaja)
             return menu()
    return menu()
menu()
