import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def raiz_cuadrada(a):
    return math.sqrt(a)

def logaritmo(a):
    return math.log10(a)

def seno(a):
    return math.sin(a)

def coseno(a):
    return math.cos(a)

def tangente(a):
    return math.tan(a)

# Función ecuación lineal
def resolver_ecuacion_lineal(a, b):
    if a == 0:
        if b == 0:
            return "La ecuación es indeterminada (0 = 0)"
        else:
            return "La ecuación es contradictoria (0 = {} no es posible)".format(b)
    else:
        x = -b / a
        return "El resultado de la ecuación {}x + {} = 0 es x = {}".format(a, b, x)

# Función principal de la calculadora
def calculadora():
    print("¡Bienvenido a la calculadora científica multifuncional!")

    while True:
        print("\nOpciones disponibles:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Raíz cuadrada")
        print("6. Logaritmo (base 10)")
        print("7. Seno")
        print("8. Coseno")
        print("9. Tangente")
        print("10. Resolver ecuación lineal de primer grado")
        print("11. Salir")

        opcion = input("Seleccione una opción (1-11): ")

        if opcion == "1":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("Resultado:", suma(a, b))
        elif opcion == "2":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("Resultado:", resta(a, b))
        elif opcion == "3":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("Resultado:", multiplicacion(a, b))
        elif opcion == "4":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("Resultado:", division(a, b))
        elif opcion == "5":
            a = float(input("Ingrese el número: "))
            print("Resultado:", raiz_cuadrada(a))
        elif opcion == "6":
            a = float(input("Ingrese el número: "))
            print("Resultado:", logaritmo(a))
        elif opcion == "7":
            a = float(input("Ingrese el ángulo en radianes: "))
            print("Resultado:", seno(a))
        elif opcion == "8":
            a = float(input("Ingrese el ángulo en radianes: "))
            print("Resultado:", coseno(a))
        elif opcion == "9":
            a = float(input("Ingrese el ángulo en radianes: "))
            print("Resultado:", tangente(a))
        elif opcion == "10":
            a = float(input("Ingrese el coeficiente a: "))
            b = float(input("Ingrese el coeficiente b: "))
            print(resolver_ecuacion_lineal(a, b))
        elif opcion == "11":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Ejecutar la calculadora
calculadora()
