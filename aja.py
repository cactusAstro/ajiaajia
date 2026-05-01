import random

secreto = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input("Adivina (1-100): "))
    intentos += 1

    if intento < secreto:
        print("El número es mayor.")
    elif intento > secreto:
        print("El número es menor.")
    else:
        print("Correcto. Intentos:", intentos)
        if intentos < 5:
            print("Lo has conseguido en menos de 5 intentos.")
        break
