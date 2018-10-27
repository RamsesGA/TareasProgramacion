def divisores():
	div=0
	num=0
	resu=0
	ciclo=0
	temp=0
	resList=[]

	if __name__ == '__main__':
		print(__name__)

	print("Ingresa un número para mostrar sus numeros divisores:")
	num=int(input())

	if (num%2==0): #si num y el residuo de 2 da 0 se hara una division entre el numero ingresado y la mitad de el, se guarda en una variable.
		resu=num/2
	for ciclo in range(1,int(resu)+1): #ciclo aumentara en rango del 1 al resultado .
		if (num%ciclo==0): #si el numero y el residuo en el ciclo que va da 0 una variable guarda el numero entre el ciclo en el que va.
			temp=num/ciclo
			if (temp!=div):#despues si esa variable es diferente a div, div tendra lo de temp.
				div=temp    
				resList.append(div) #Por ultimo una lista tomara los datos consecutivamente de div y los mostrara.
	print("Tu numero:\n",num,"\n","Lista final:\n",resList)

divisores()
	