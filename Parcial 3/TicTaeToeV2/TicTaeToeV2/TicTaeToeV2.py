import os
import time
import random

#Menu
def menu():
    with open('historial.txt', 'r') as histo:
         for line in histo:
             histo.readline()
    print("---Bienvenido al menu ingresa---\n0-Para salir\n1-Para iniciar PvP\n2-Para iniciar Player vs IA")
    valor = str(input())
    #Chequeo para solo numeros.
    if valor.isnumeric() == True:
        valor2 = int(valor)
        if valor2 == 0:
            print("---Adios---")
            SystemExit()
        elif valor2 == 1:
            pvp()
        elif valor2 == 2:
            ia()
        elif valor2 >=3:
            print("Numero fuera del rango")
            time.sleep(1)
            os.system('cls')
            return menu()
    else:
        print("E R R O R, ingreso un valor invalido")
        time.sleep(1)
        os.system('cls')
        return menu()

def pvp():
    global Pun1 
    global Pun2
    global CPU 
    global emp 
    j1 = []
    p1 = 'X'
    j2 = []
    p2 = 'Z'
    uno = 0
    intentos = 0
    listDib = [0,1,2,3,4,5,6,7,8] 
    
    while intentos <= 9:
#Jugador 1
        print("Jugador 1, ingresa un valor de 0 a 8")
        check = str(input())
#Check solo para valores numericos
        if check.isnumeric() == True:
            j1 = check
            check = int(check)
            if check <= 8:
                j1 = int(j1)
                while j1 not in listDib:
                    print("Valor repetido, ingresa otro numero: ")
                    j1 = list(input()) 
                while j1 in listDib:
                        listDib.pop(j1)
                        listDib.insert(j1, p1)     
                        print(listDib[0],"|", listDib[1],"|", listDib[2])
                        print("---------")
                        print(listDib[3],"|", listDib[4],"|", listDib[5])
                        print("---------")
                        print(listDib[6],"|", listDib[7],"|", listDib[8])
                        intentos = intentos + 1
                        
#Romper ciclo 
        if intentos == 9:
            print("---Empate---")
            emp = emp + 1
            historial()
            return menu()
#Condiciones de victoria JUGADOR 1 Horizontal
        if listDib[0] == 'X' and listDib[1] == 'X' and listDib[2] == 'X':
           print("Victoria del jugador 1")
           Pun1 = Pun1 + 1
           historial()
           return menu()
        elif listDib[3] == 'X' and listDib[4] == 'X' and listDib[5] == 'X':
           print("Victoria del jugador 1")
           Pun1 = Pun1 + 1
           historial()
           return menu()
        elif listDib[6] == 'X' and listDib[7] == 'X' and listDib[8] == 'X':
           print("Victoria del jugador 1")
           Pun1 = Pun1 + 1
           historial()
           return menu()
# V E R T I C A L
        elif listDib[0] == 'X' and listDib[3] == 'X' and listDib[6] == 'X':
           print("Victoria del jugador 1")
           Pun1 = Pun1 + 1
           historial()
           return menu()
        elif listDib[1] == 'X' and listDib[4] == 'X' and listDib[7] == 'X':
           print("Victoria del jugador 1")
           Pun1 = Pun1 + 1
           historial()
           return menu()
        elif listDib[2] == 'X' and listDib[5] == 'X' and listDib[8] == 'X':
           print("Victoria del jugador 1")
           Pun1 = Pun1 + 1
           historial()
           return menu()
# D I A G O N A L
        elif listDib[0] == 'X' and listDib[4] == 'X' and listDib[8] == 'X':
           print("Victoria del jugador 1")
           Pun1 = Pun1 + 1
           historial()
           return menu()
        elif listDib[2] == 'X' and listDib[4] == 'X' and listDib[6] == 'X':
           print("Victoria del jugador 1")
           Pun1 = Pun1 + 1
           historial()
           return menu()
#Jugador 2
        print("Jugador 2, ingresa un valor del 0 al 8")
        check2 = str(input())
#Check solo para valores numericos
        if check2.isnumeric() == True:
           j2 = check2
           check2 = int(check2)
           if check2 <= 8:
              j2 = int(j2)
              while j2 not in listDib:
                  print("Valor repetido, ingrese un numero: ")
                  j2 = list(input())
              while j2 in listDib:
                     listDib.pop(j2)
                     listDib.insert(j2, p2)
                     print(listDib[0],"|", listDib[1],"|", listDib[2])
                     print("---------")
                     print(listDib[3],"|", listDib[4],"|", listDib[5])
                     print("---------")
                     print(listDib[6],"|", listDib[7],"|", listDib[8])
                     intentos = intentos + 1
                     
#Condiciones de victoria JUGADOR 2 --- H O R I Z O N T A L
        if listDib[0] == 'Z' and listDib[1] == 'Z' and listDib[2] == 'Z':
           print("Victoria del jugador 2")
           Pun2 = Pun2 + 1
           historial()
           return menu()
        elif listDib[3] == 'Z' and listDib[4] == 'Z' and listDib[5] == 'Z':
           print("Victoria del jugador 2")
           Pun2 = Pun2 + 1
           historial()
           return menu()
        elif listDib[6] == 'Z' and listDib[7] == 'Z' and listDib[8] == 'Z':
           print("Victoria del jugador 2")
           Pun2 = Pun2 + 1
           historial()
           return menu()
# V E R T I C A L
        elif listDib[0] == 'Z' and listDib[3] == 'Z' and listDib[6] == 'Z':
           print("Victoria del jugador 2")
           Pun2 = Pun2 + 1
           historial()
           return menu()
        elif listDib[1] == 'Z' and listDib[4] == 'Z' and listDib[7] == 'Z':
           print("Victoria del jugador 2")
           Pun2 = Pun2 + 1
           historial()
           return menu()
        elif listDib[2] == 'Z' and listDib[5] == 'Z' and listDib[8] == 'Z':
           print("Victoria del jugador 2")
           Pun2 = Pun2 + 1
           historial()
           return menu()
# D I A G O N A L
        elif listDib[0] == 'Z' and listDib[4] == 'Z' and listDib[8] == 'Z':
           print("Victoria del jugador 2")
           Pun2 = Pun2 + 1
           historial()
           return menu()
        elif listDib[2] == 'Z' and listDib[4] == 'Z' and listDib[6] == 'Z':
           print("Victoria del jugador 2")
           Pun2 = Pun2 + 1
           historial()
           return menu()
            #Else segundo IF
#            else:
 #               print("E R R O R, valor fuera de rango")
   #             time.sleep(1)
    #            os.system('cls')
     #           return pvp()
      #  #Else primer IF
       # else:
        #    print("E R R O R, ingreso un valor invalido")
         #   time.sleep(1)
          #  os.system('cls')
           # return pvp()




#Función "Ia"
def ia():
    global Pun1 
    global Pun2
    global CPU 
    global emp 
    j1 = []
    p1 = 'X'
    j2 = []
    p2 = 'Z'
    uno = 0
    intentos = 0
    listDib = [0,1,2,3,4,5,6,7,8]
    caja = [0,1,2,3,4,5,6,7,8]
    cajita = 0
    
    while intentos <= 9:
#Jugador 1
        print("Jugador 1, ingresa un valor de 0 a 8")
        check = str(input())
#Check solo para valores numericos
        if check.isnumeric() == True:
            j1 = check
            check = int(check)
            if check <= 8:
                j1 = int(j1)
                while j1 not in listDib:
                    print("Valor repetido, ingresa otro numero: ")
                    j1 = list(input()) 
                while j1 in listDib:
                        listDib.pop(j1)
                        listDib.insert(j1, p1)    
                        caja.remove(j1)
                        print(listDib[0],"|", listDib[1],"|", listDib[2])
                        print("---------")
                        print(listDib[3],"|", listDib[4],"|", listDib[5])
                        print("---------")
                        print(listDib[6],"|", listDib[7],"|", listDib[8])
                        intentos = intentos + 1
                        
#Romper ciclo 
        if intentos == 9:
            print("---Empate---")
            emp = emp + 1
            historial()
            return menu()
#Condiciones de victoria JUGADOR 1 Horizontal
        if listDib[0] == 'X' and listDib[1] == 'X' and listDib[2] == 'X':
           print("Victoria del jugador 1")
           Pun1 = Pun1 + 1
           historial()
           return menu()
        elif listDib[3] == 'X' and listDib[4] == 'X' and listDib[5] == 'X':
           print("Victoria del jugador 1")
           Pun1 = Pun1 + 1
           historial()
           return menu()
        elif listDib[6] == 'X' and listDib[7] == 'X' and listDib[8] == 'X':
           print("Victoria del jugador 1")
           Pun1 = Pun1 + 1
           historial()
           return menu()
# V E R T I C A L
        elif listDib[0] == 'X' and listDib[3] == 'X' and listDib[6] == 'X':
           print("Victoria del jugador 1")
           Pun1 = Pun1 + 1
           historial()
           return menu()
        elif listDib[1] == 'X' and listDib[4] == 'X' and listDib[7] == 'X':
           print("Victoria del jugador 1")
           Pun1 = Pun1 + 1
           historial()
           return menu()
        elif listDib[2] == 'X' and listDib[5] == 'X' and listDib[8] == 'X':
           print("Victoria del jugador 1")
           Pun1 = Pun1 + 1
           historial()
           return menu()
# D I A G O N A L
        elif listDib[0] == 'X' and listDib[4] == 'X' and listDib[8] == 'X':
           print("Victoria del jugador 1")
           Pun1 = Pun1 + 1
           historial()
           return menu()
        elif listDib[2] == 'X' and listDib[4] == 'X' and listDib[6] == 'X':
           print("Victoria del jugador 1")
           Pun1 = Pun1 + 1
           historial()
           return menu()
#Jugador 2
        print("---CPU----")
        cajita = random.choice(caja)
        while cajita in listDib:
            listDib.pop(cajita)
            listDib.insert(cajita, p2)
            caja.remove(cajita)
            print(listDib[0],"|", listDib[1],"|", listDib[2])
            print("---------")
            print(listDib[3],"|", listDib[4],"|", listDib[5])
            print("---------")
            print(listDib[6],"|", listDib[7],"|", listDib[8])
            intentos = intentos + 1                     
#Condiciones de victoria JUGADOR 2 --- H O R I Z O N T A L
        if listDib[0] == 'Z' and listDib[1] == 'Z' and listDib[2] == 'Z':
           print("Victoria del jugador 2")
           CPU = CPU + 1
           historial()
           return menu()
        elif listDib[3] == 'Z' and listDib[4] == 'Z' and listDib[5] == 'Z':
           print("Victoria del jugador 2")
           CPU = CPU + 1
           historial()
           return menu()
        elif listDib[6] == 'Z' and listDib[7] == 'Z' and listDib[8] == 'Z':
           print("Victoria del jugador 2")
           CPU = CPU + 1
           historial()
           return menu()
# V E R T I C A L
        elif listDib[0] == 'Z' and listDib[3] == 'Z' and listDib[6] == 'Z':
           print("Victoria del jugador 2")
           CPU = CPU + 1
           historial()
           return menu()
        elif listDib[1] == 'Z' and listDib[4] == 'Z' and listDib[7] == 'Z':
           print("Victoria del jugador 2")
           CPU = CPU + 1
           historial()
           return menu()
        elif listDib[2] == 'Z' and listDib[5] == 'Z' and listDib[8] == 'Z':
           print("Victoria del jugador 2")
           PCPU = CPU + 1
           historial()
           return menu()
# D I A G O N A L
        elif listDib[0] == 'Z' and listDib[4] == 'Z' and listDib[8] == 'Z':
           print("Victoria del jugador 2")
           CPU = CPU + 1
           historial()
           return menu()
        elif listDib[2] == 'Z' and listDib[4] == 'Z' and listDib[6] == 'Z':
           print("Victoria del jugador 2")
           CPU = CPU + 1
           historial()
           return menu()

def historial():
   global Pun1 
   global Pun2 
   global CPU 
   global emp 
   with open('histo.txt', 'w') as histo2:
      histo2.write("Jugador 1\n")
      Pun1 = str(Pun1)
      histo2.write(Pun1)
      histo2.write("\nJugador 2\n")
      Pun2 = str(Pun2)
      histo2.write(Pun2)
      histo2.write("\nPC\n")
      CPU = str(CPU)
      histo2.write(CPU)
      histo2.write("\nEmpate\n")
      emp = str(emp)
      histo2.write(emp)


if __name__ == '__main__':
  Pun1 = 0
  Pun2 = 0
  CPU = 0
  emp = 0
  menu()