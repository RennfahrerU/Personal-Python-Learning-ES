import random
import bancoOperaciones

print("Bienvenido al banco Lorro Bamos")

print("En primer lugar, cree su cuenta.")
# nombre = input("Ingrese su nombre: ")
# apellido = input("Ingrese su apellido: ")
nombre = "Yilver"
apellido = "Rivera"
# saldo = random.randint(500000, 2450000)
saldo = 1000
uso = True

print("Bienvenido al banco " + nombre + " " + apellido)
print("¿Qué desea hacer?")
op = int(input("1. Mostrar el saldo \n2. Depositar en su cuenta \n3. Retirar de su cuenta \n4. Salir del programa\nOpción:"))

while uso is True:
    if op == 1:
        bancoOperaciones.consultar(saldo)
    elif op == 2:
        saldo = bancoOperaciones.depositar(saldo)
    elif op == 3:
        saldo = bancoOperaciones.retirar(saldo)
    elif op == 4:
        uso = False
    else:
        print("Opcion no valida")
    op = int(input("1. Mostrar el saldo \n2. Depositar en su cuenta \n3. Retirar de su cuenta \n4. Salir del programa\nOpción:"))

k = input("press close to exit")
