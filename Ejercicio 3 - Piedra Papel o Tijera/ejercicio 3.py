# pylint: disable=C0103

import random
import time
mano = ["PIEDRA", "PAPEL", "TIJERAS"]

# print(mano[0])
# print(random.choice(mano))

jugar = True
nombre = input("Ingrese su nombre: ")

while jugar is True:
    manoIA = random.choice(mano)
    manojugador = input("¿Qué va a sacar de: " + str(mano) + "? ")
    manojugador = manojugador.upper()
    # manojugador = "PIEDRA"

    while manojugador.upper() not in str(mano):
        manojugador = input(
            "Entrada inválida. Por favor responda con PIEDRA, PAPEL O TIJERAS: ")
        manojugador = manojugador.upper()

    print("\nLa IA está escogiendo su mano...")
    time.sleep(1.5)
    print("La IA escogió " + manoIA)
    time.sleep(0.5)
    if manojugador == mano[0]:
        if manoIA == mano[0]:
            print("Hay empate.\n")

        elif manoIA == mano[1]:
            print("¡Gana la IA!\n")

        else:
            print("¡Gana " + nombre + "!\n")

    if manojugador == mano[1]:
        if manoIA == mano[0]:
            print("¡Gana " + nombre + "!\n")

        elif manoIA == mano[1]:
            print("Hay empate.\n")

        else:
            print("¡Gana la IA!\n")

    if manojugador == mano[2]:
        if manoIA == mano[0]:
            print("¡Gana la IA!\n")

        elif manoIA == mano[1]:
            print("¡Gana " + nombre + "!\n")

        else:
            print("Hay empate.\n")

    entradajugar = input(nombre + ", ¿Desea jugar otra ronda? Reponda S o N: ")
    while entradajugar.upper() not in ["S", "N"]:
        entradajugar = input(
            "Entrada inválida. Por favor responda con S o N: ")

    if entradajugar.upper() == "N":
        jugar = False
