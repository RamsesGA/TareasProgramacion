def listas():
	lista1=[1,1,2,3,5,8,13,21,34,55,89]
	lista2=[1,2,3,4,5,6,7,8,9,10,11,12,13]
	lista3=[]
	resu=[]
	ciclo=0
	comp=0

	#For uno que ingrese primero los valores de L2 
	for ciclo in lista2:
		#If que compare los valores de L2 y L1 y guardamos en una lista el reusltado
		if ciclo in lista1:
			resu.append(ciclo)
	#If de los 6 valores obtenidos comparas si 6>0 y entrar a un For
	if (len(resu)>comp):
		#For de 1 valor hasta 6 va a agregar esos valores a L3
		for ciclo in resu:
			lista3.append(ciclo)
		print("Estos numeros comparten ambas listas:\n",lista3)
listas()