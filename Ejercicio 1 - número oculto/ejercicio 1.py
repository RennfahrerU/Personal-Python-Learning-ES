# pylint: disable=C0103

import random

num_oculto = random.randint(1, 10)
intento = 0
adivinado = False
jugar = True
# print (num_oculto)

print("Debes adivinar el número oculto entre 1 y 10.\n")
while jugar:
    while not adivinado:
        entrada = int(input("Ingrese el número que cree que es: "))
        if entrada < num_oculto:
            print("El número es menor al oculto.\n")
            intento += 1
        elif entrada > num_oculto:
            print("El número es mayor al oculto.\n")
            intento += 1
        else:
            print("Ha adivinado el número " + str(num_oculto) + "!")
            intento += 1
            adivinado = True
    print("Lo ha hecho en " + str(intento) + " intentos.")

    entradajugar = input("¿Desea jugar otra ronda? Reponda S o N: ")
    while entradajugar.upper() not in ["S", "N"]:
        entradajugar = input(
            "Entrada inválida. Por favor responda con S o N: ")

    if entradajugar.upper() == "N":
        jugar = False
    else:
        num_oculto = random.randint(1, 10)
        intento = 0
        adivinado = False
