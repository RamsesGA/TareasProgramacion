def menu():
    print("Bienvenido, ingrese\n1-Factorial\n2-Multiplicación\n")
    valor = int(input())

    if valor == 1:
        print("Ingresa un numero: ")
        num = int(input())
        print("El numero factorial de:", num, "es:", facto(num))
    elif valor == 2:
        print("Ingrese el valor inicial a multiplicar: ")
        num2 = int(input())
        print("Ingresa el numero a multiplicar: ")
        num3 = int(input())
        num4 = num2 * num3
        multi(num2, num3, num4)
        print(multi(num2, num3, num4))

def facto(num : int):
    if num == 1:
        return 1
    return num * facto(num - 1)

def multi(num2 : int, num3 : int, num4 : int):
    if num2 == num4:
        return num2
    else:
        num2 = num2 + num3
        return multi(num2, num3, num4)
    

menu()


