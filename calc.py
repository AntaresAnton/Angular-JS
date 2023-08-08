# Pedimos al usuario que introduzca dos números
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Mostramos las opciones disponibles
print("Selecciona una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

# Pedimos al usuario que seleccione una opción
opcion = int(input("Introduce tu opción (1/2/3/4): "))

# Realizamos la operación seleccionada por el usuario
if opcion == 1:
    resultado = num1 + num2
elif opcion == 2:
    resultado = num1 - num2
elif opcion == 3:
    resultado = num1 * num2
elif opcion == 4:
    resultado = num1 / num2
else:
    print("Opción inválida, por favor introduce una opción válida")

# Mostramos el resultado
print("El resultado es:", resultado)
