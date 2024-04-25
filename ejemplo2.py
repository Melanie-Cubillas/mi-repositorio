def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero = int(input("Ingresa un número para calcular su factorial: "))
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")
