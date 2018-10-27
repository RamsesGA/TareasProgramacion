def Fibo():
	numIni=1
	numSeg=0
	numUlti=0
	numFibo=0

	if __name__ == '__main__':
		print(__name__)
		
	print("-Bienvenido humano a la secuancia Fibonacci hasta el 10-")

	print("-",numSeg,"-")
	print("-",numIni,"-")

	while numFibo<=7:
		numSeg=numUlti
		numUlti=numIni
		numIni=numSeg+numUlti
		print("-",numIni,"-")
		numFibo=numFibo+1
Fibo()