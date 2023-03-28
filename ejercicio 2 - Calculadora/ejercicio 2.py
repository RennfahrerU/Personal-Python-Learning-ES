import operaciones
import time

print("Bienvenido a la calculadora, ingrese sus dos números a operar.")

num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
opcion = int(input(
    "¿Qué operación quiere hacer?: \n 1. Suma \n 2. Resta \n 3. Multiplicación \n 4. División\n"))


def operacion(opcion):
    dict_op = {
        1: operaciones.suma(num1, num2),
        2: operaciones.resta(num1, num2),
        3: operaciones.multiplicacion(num1, num2),
        4: operaciones.division(num1, num2)
    }
    return dict_op[opcion]


res = operacion(opcion)
print("El resultado es:", res)
time.sleep(5)
