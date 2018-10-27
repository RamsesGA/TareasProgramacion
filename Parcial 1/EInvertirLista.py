def menu():
	val=0
	val=int(input("---Ingresa 1- Para el primer programa---\n---2- Para el segundo---\n"))

	if val == 1:
		uno()
	if val == 2:
		dos()

def uno():
	#Una manera

	lista=[1,2,3,4,5]
	cubeta=[]

	for ciclo in range(len(lista)):
		cubeta.insert(0,ciclo)
	print("Lista inversa",cubeta)


def dos():

	print("Algo")

menu()