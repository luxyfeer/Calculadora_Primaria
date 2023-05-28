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

def resolver_ecuacion_lineal(a, b):
    if a == 0:
        if b == 0:
            return "La ecuación es indeterminada (0 = 0)"
        else:
            return "La ecuación es contradictoria (0 = {} no es posible)".format(b)
    else:
        x = -b / a
        return "El resultado de la ecuación {}x + {} = 0 es x = {}".format(a, b, x)

def calcular_promedio_dos_numeros(a, b):
    return (a + b) / 2

def calcular_promedio_tres_numeros(a, b, c):
    return (a + b + c) / 3

def encontrar_maximo(a, b):
    return max(a, b)

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
        print("11. Calcular promedio de dos números")
        print("12. Calcular promedio de tres números")
        print("13. Encontrar máximo de dos números")
        print("14. Salir")

        opcion = input("Seleccione una opción (1-14): ")

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
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("El promedio de los dos números es:", calcular_promedio_dos_numeros(a, b))
        elif opcion == "12":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            c = float(input("Ingrese el tercer número: "))
            print("El promedio de los tres números es:", calcular_promedio_tres_numeros(a, b, c))
        elif opcion == "13":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("El máximo de los dos números es:", encontrar_maximo(a, b))
        elif opcion == "14":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Ejecutar la calculadora
calculadora()
