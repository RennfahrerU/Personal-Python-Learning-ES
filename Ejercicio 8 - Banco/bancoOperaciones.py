def consultar(s):
    print("\nTiene " + str(s) + " pesos en su cuenta actualmente." + "\n")


def depositar(s):
    dep = int(input("\nIngrese el valor a depositar: "))
    s = s + dep
    print("Acaba de depositar: " + str(dep) +
          "\nSu nuevo saldo es de: " + str(s) + "\n")
    return s


def retirar(s):
    ret = int(input("\nIngrese el valor a retirar: "))
    s = s - ret
    print("Acaba de retirar: " + str(ret) +
          "\nSu nuevo saldo es de: " + str(s) + "\n")
    return s
