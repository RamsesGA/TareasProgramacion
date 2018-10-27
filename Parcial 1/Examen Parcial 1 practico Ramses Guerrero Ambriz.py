def menu():
	valor=0

	print("Bienvenido al menu ingresa un numero para ejecutar el programa-----\n 1: Función la cual invierte elementos \n 2: Palabras palíndromas")
	valor=int(input())

	print("Usted ingreso", valor)

	
	if valor == 1:
		invertido()
		valor == 0
	elif valor == 2:
		palin()
		valor == 0


def invertido():
	firstList=["6,5,4,3,2,1"]

	for ciclo in range(len(firstList)):
		#[inicio:fin:y un incremento negativo] no debo poner valores adentro ya que asumira que inicio es el final y el final el inicio
		cubeta=[firstList[ciclo][::-1]]
	print(cubeta)
	

def palin():
	cubeta=[]
	cubetita=[]

	#Pide al usuario un valor y lo gurado en una variable
	Pali=input("Ingresa un palindromo: ")
	#listPali tomará el valor de Pali convertido en una lista y lo imprimimos
	listPali=list((Pali))
	print(listPali)

	#cubetita tomara los valores en cantidad 
	cubetita=len(listPali)

	#Hago un ciclo de 0 a los valores que tiene cubetita
	for ciclo in range(cubetita):
		#cubeta tendra los valores de listPali pero aun no me queda ca
		cubeta.append(listPali[cubetita-ciclo-1])
	print(cubeta)
	if listPali == cubeta:
		print("Es palindromo :c")
	else:
		print("No es palindromo :c")



menu()
