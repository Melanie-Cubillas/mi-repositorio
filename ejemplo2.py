def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

num = int(input("Ingresa un número para calcular su factorial: "))
resultado = factorial(num)
print(f"El factorial de {num} es {resultado}")

