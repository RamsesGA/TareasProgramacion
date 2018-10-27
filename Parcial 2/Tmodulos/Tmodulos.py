import random
import datetime
import time


def randomNum(start, end): #Funcion para dar un numero aleatorio del 0 al 100
    num = random.randint(start, end)
    return num


if __name__ == "__main__":
    print("numero random:", randomNum(0, 100))
    myDate = datetime.date(2000, 8, 15)
    print("Día de hoy:", myDate.today())
