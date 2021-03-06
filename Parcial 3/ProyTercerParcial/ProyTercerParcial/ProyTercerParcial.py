from os import path


#Clase para poder almacenar datos de cada niño, imprimir los datos correctos de esté.
class Alumnos():
   def __init__(self, nombre2 : str, cali2 : float, GG : str):
       self.nombre = nombre2
       self.cali = cali2
       self.gradoGrupo = GG
   def string(self):
       transformacion = ""
       transformacion = self.nombre + ' ' + self.cali + ' ' + self.gradoGrupo + '\n'
       return transformacion
   def imprimir(self):
       print("Nombre: ", self.nombre, " Promedio: ", self.cali, " Grado y grupo: ", self.gradoGrupo)
#Clase para asignar el grupo especifico que se recibe y los datos de todos los niños.
class GruposAlumnos():
    def __init__(self, NombreGrupo):
        self.elGrupo = NombreGrupo
        self.battleRoyal = []
    #Función para poder crear el archivo de texto.
    def nameGrupo(self):
        return self.elGrupo + ".txt"     
#Función para poder checar si el grupo existe o no.
def checkGroup(allGroups, futureGroups):
    for x in allGroups:
        if x.elGrupo == futureGroups:
            return 1
    return -1
#Función para poder imprimir todos los alumnos.
def imprimirDefinitivo(listNiños):
    for x in listNiños:
        for i in x.battleRoyal:
            i.imprimir()
#Función para poder organizar por calificación
def ordenCali(long):
        numMayor = 0
        reserva = 0
        for x in long:
            for i in range(0, len(x.battleRoyal) - 1):
                numMayor = float(x.battleRoyal[i].cali)
                reserva = i
                for j in range(i + 1, len(x.battleRoyal)):
                    if (float(x.battleRoyal[j].cali) < numMayor):
                        numMayor = float(x.battleRoyal[j].cali)
                        reserva = j
                x.battleRoyal[reserva], x.battleRoyal[i] = x.battleRoyal[i], x.battleRoyal[reserva]
        imprimirDefinitivo(long)
        for k in long:
            with open(k.nameGrupo(), 'w') as arch:
                for l in k.battleRoyal:
                    arch.write(l.string())

#Función para poder ordenar por abecedario.
def abecedario(long2):
    wordMayor = 0
    reserva = 0
    for x in long2:
        for i in range(0, len(x.battleRoyal) - 1):
            wordMayor = x.battleRoyal[i].nombre
            reserva = i
            for j in range(i + 1, len(x.battleRoyal)):
                if (x.battleRoyal[j].nombre < wordMayor):
                    wordMayor = x.battleRoyal[j].nombre
                    reserva = j
            x.battleRoyal[reserva], x.battleRoyal[i] = x.battleRoyal[i], x.battleRoyal[reserva]
    imprimirDefinitivo(long2)
    for k in long2:
            with open(k.nameGrupo(), 'w') as arch:
                for l in k.battleRoyal:
                    arch.write(l.string())
#
def main():
    print("Ingresa\n0-Salir\n1-Iniciar el programa\n")
    valor = str(input())
    if valor.isdecimal() == True:
        valor = int(valor)
        if valor == 0:
            SystemExit()
        elif valor == 1:
            principal()
        elif valor >=2:
            print("Valor mayor al solicitado...")
            return main()
    else:
        print("- - - - - -Valor no permitido- - - - - ")
        return main()
#
def principal():
    x = 0
    parametro = None
    listAllKids = []
    strNewBoy = ""
    verify = path.isfile("alumnos.txt")
    if verify:        
        #Darle los valores del archivo a una variable.
        with open('alumnos.txt') as archivoAlumnos:
            lineaArchivo = archivoAlumnos.readline()

            #Ciclo para asignar un alumno a la vez y enviarlo a la clase.
            while lineaArchivo:
                lineaArchivo = lineaArchivo.split()

                #Enviar los datos de un alumno a la clase.
                parametro = Alumnos(lineaArchivo[0], lineaArchivo[1], lineaArchivo[2])

                #Condición para confirmar si existe o no el grupo.
                if checkGroup(listAllKids, parametro.gradoGrupo) == 1:
                    for x in listAllKids:
                        if x.elGrupo == parametro.gradoGrupo:
                            x.battleRoyal.append(parametro)
                else:
                    #Al abrir el archivo vacio, la variable elGrupo recibe un valor.
                    GrupitoNuevo = GruposAlumnos(parametro.gradoGrupo)
                    #le damos un valor a battleRoyal de 1 alumno completo.
                    GrupitoNuevo.battleRoyal.append(parametro)
                    #Está variable tendra todos los niños, paso por paso.y
                    listAllKids.append(GrupitoNuevo)
                lineaArchivo = archivoAlumnos.readline()
                #F I N.

        #Crear archivos.
        for x in listAllKids:
            with open(x.nameGrupo(), 'w') as arch:
                for i in x.battleRoyal:
                    arch.write(i.string())
    else:
        print("Error, archivo no encontrado, se recomienda ingresarlo")
    #Inicia la interfaz uwu.
    print("Ingresa\n0-Salir\n1-Ingresar un nuevo alummno\n2-Ver todos los alumnos\n3-Ordenar numericamente\n4-Ordenar por alfabeto\n")
    valor = str(input())
    #Valores para el menu.
    if valor.isdecimal() == True:        
        valor = int(valor)
        if valor == 0:
            print("Nos vemos...")
            SystemExit()
        elif valor == 1:
            print("Ingresa un nuevo alummno con sus siguientes datos...")
            print("Nombre: ")
            niño = str(input())
            niño = niño.capitalize()
            if niño.isalpha() == True:
                print("Calificación: ")
                califi = input()
                try:
                    califi = float(califi)
                    print("Año: ")
                    A = str(input())
                    if A.isdecimal() == True:
                        print("Ingresa la letra del grupo")
                        G = str(input())
                        if G.isalpha() == True:
                            G = G.upper()
                            califi = str(califi)
                            strNewBoy = (niño + ' ' + califi + ' ' + A + G)
                            with open("alumnos.txt", 'a') as niñoNew:
                                niñoNew.write('\n')
                                niñoNew.write(strNewBoy)
                        else:
                            print("Valor incorrecto\n")
                            principal()
                    else:
                        print("Valor incorrecto\n")
                        principal
                except:
                    print("Valor incorrecto\n")
                    principal()
            else:
                print("Valor incorrecto\n")
                principal()
        elif valor == 2:
            print("---------Listas completas---------")
            imprimirDefinitivo(listAllKids)
            print("---------Lista total terminada---------\n")
            principal()
        elif valor == 3:          
            print("----------Listas ordenadas numericamente--------")
            ordenCali(listAllKids)
            print("---------Lista total terminada---------\n")
            principal()
        elif valor == 4:
            print("---------Listas ordenadas alfabeticamente----------")
            abecedario(listAllKids)
            print("---------Lista total terminada---------\n")
            principal()
        elif valor >= 5:
            print("---------Valor fuera de rango---------\n")
            principal()
    else:
        print("---------Ingresa un valor correcto----------\n")
        return principal()
main()