# Calculadora simple
while True:
    operacion = input("Elige una operación (suma, resta, multiplicación, división) o 'salir' para terminar: ")
    if operacion == "salir":
        print("¡Hasta luego!")
        break

    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if operacion == "suma":
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")
    elif operacion == "resta":
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")
    elif operacion == "multiplicación":
        resultado = num1 * num2
        print(f"{num1} × {num2} = {resultado}")
    elif operacion == "división":
        if num2 == 0:
            print("Error: no se puede dividir entre cero.")
        else:
            resultado = num1 / num2
            print(f"{num1} ÷ {num2} = {resultado}")
    else:
        print("Operación no válida. Usa: suma, resta, multiplicación, división o salir.")
