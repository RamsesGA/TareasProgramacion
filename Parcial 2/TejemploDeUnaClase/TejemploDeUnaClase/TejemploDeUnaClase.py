#Ejemplo de como usar una clase en python UwU

class Auto:
	#Init es una funcion a la cual llamamos inicializador o constructor.
	#Self es una varibale la cual hace referencia hacia el mismo;
	# o el objeto a la cual hace llamar la funcion.
	def __init__(self, color : str, numAsientos : int, numCilindros : int, numLlantas : int, numPlacas : str, numPuertas :int):
		self.numLlantas = numLlantas
		self.numPuertas = numPuertas
		self.color = color
		self.numPlacas = numPlacas
		self.numAsientos = numAsientos
		self.numCilindros = numCilindros

def main():
    mustang = Auto()
    print(mustang.numPlacas)

    print()

    pass

if __name__ == "__main__":
	main()