def complicado():
	numberList=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	elementList=[]
	limitList=[]
	element=0
	numberLimit=0
	number=0

	if __name__ == '__main__':
		print(__name__)
	#Todos los numeros que sean menores a 5 de manera automatica
	print("----Ejercicio 1-----")
	for element in numberList:
		if (element<6):
			print(element)
			elementList.append(element)
			element=element+1

	#Todos los numero deben estar en la misma hilera
	print("-----Ejercicio 2-----")
	elementList.append(element)	
	elementList.pop(5)
	print(elementList)

	#Pedir al usuario el número límite
	print("-----Ejercicio 3-----")
	print("Bienvenido Humano, ingresa un número límite")
	numberLimit=int(input())
	for number in numberList:
		if (number<numberLimit):
			limitList.append(number)
	print("Los numeros serían:\n",limitList)

	#Generar una lista con la secuencia Fibonacci preguntando cuantos elementos debe contener
	print("-----Ejercicio 4-----")
	numIni=1
	numSeg=0
	numUlti=0
	numFibo=0
	aum=0
	fiboList=[]
	print("Bienvenido Humano, ingresa un número para el Fibonacci")
	numFibo=int(input())
	print("-",numSeg,"-")
	print("-",numIni,"-")
	fiboList.append(numSeg)
	fiboList.append(numIni)
	numFibo=numFibo-2
	while aum<numFibo:
		numSeg=numUlti
		numUlti=numIni
		numIni=numSeg+numUlti
		print("-",numIni,"-")
		fiboList.append(numIni)
		aum=aum+1
	numFibo=numFibo+2
	print("El resultado del valor", numFibo,"en una lista:\n", fiboList)
complicado()