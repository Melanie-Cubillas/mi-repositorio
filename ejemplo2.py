def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

numero = int(input("Ingresa un número para calcular su factorial: "))
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")

