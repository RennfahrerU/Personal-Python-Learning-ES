import random
import time

palabras = ["BUENA", "FORMA", "MEDIO", "PUNTO", "MUNDO"]
ahorcado = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
adivina = "_____"  # Escoger palabra al azar de la lista
palabraEscondida = random.choice(palabras)
intentos = 0

print("Juego del ahorcado.")
print(ahorcado[0])

# Mientras haya una barra baja (es decir, que no se haya adivinado la palabra) siga ejecutando.
while "_" in adivina:
    # Mientras sea verdadero (para que siempre se pida entrada de un sólo carácter) hasta que se ingrese uno y no varios hace el break.
    while True:
        letra = input("Escriba la letra a adivinar: ")
        if len(letra) == 1:  # Si el largo de la entrada es 1 sigue el programa
            break
        else:  # Si el largo de la entrada es más de 1 vuelve a pedirla
            print("Ingrese un sólo carácter")
            continue
    letra = letra.upper()  # Convierte la entrada en mayúscula
    # Busca el índice de la letra ingresada en la palabra oculta
    indice = palabraEscondida.find(letra)
    if indice != -1:  # Si se encontró el índice reemplaza la raya baja con  la letra ingresada
        adivina = adivina[:indice] + \
            letra + adivina[indice+1:]
        # Se resta el intento de la iteración para que no afecte acertar la letra
        intentos = intentos - 1
    intentos += 1  # Suma un nuevo intento en la iteración
    if intentos == 7:  # Si se terminan los intentos se pierde y se para el while
        print("Ha perdido.")
        print("La palabra era: " + palabraEscondida)
        break
    if "_" not in adivina:  # Si no hay rayas bajas, es decir que se gana y termina el while
        intentos += -1
        print("Ha ganado con " + str(intentos) + " intentos.")
        print("La palabra era: " + palabraEscondida)
        break
    intentosDown = 7 - intentos
    print("Le quedan " + str(intentosDown) +
          " intentos.\n" + ahorcado[intentos])
    print(adivina)

time.sleep(5)
# palabra.find("")  # posicion
# palabra.replace("coincidencia", "cambio")  # Cambiar
