def Años():
	name=0
	año=0
	edad=0
	añoFinal=0

	if __name__ == '__main__':
		print(__name__)
		
	#Bienvenida y nombre
	print("-Bienvenido ser humano-")
	print("Ingrese su nombre porfavor: ")
	name=input()
	#Fin

	#Ingresar año, edad
	print("Ingrese el año actual: ")
	año=int(input())

	print("Ingrese su edad: ")
	edad=int(input())
	#Fin

	#Resultado final
	añoFinal=(año-edad)+100

	print(name," usted tendra 100 años en:\n",añoFinal)

Años()