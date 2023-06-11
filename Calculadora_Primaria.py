import math

class Calculadora:
    def __init__(self):
        self.opciones = {
            "1": self.sumar,
            "2": self.restar,
            "3": self.multiplicar,
            "4": self.dividir,
            "5": self.calcular_promedio,
            "6": self.sumar_fracciones,
            "7": self.salir
        }

    def sumar(self):
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 + num2
        print("Resultado:", resultado)

    def restar(self):
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 - num2
        print("Resultado:", resultado)

    def multiplicar(self):
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 * num2
        print("Resultado:", resultado)

    def dividir(self):
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 / num2
        print("Resultado:", resultado)

    def calcular_promedio(self):
        num_numeros = int(input("Ingrese la cantidad de números: "))
        numeros = []
        for i in range(num_numeros):
            numero = float(input("Ingrese el número {}: ".format(i+1)))
            numeros.append(numero)
        resultado = sum(numeros) / len(numeros)
        print("Resultado:", resultado)

    def sumar_fracciones(self):
        num1 = float(input("Ingrese el numerador de la primera fracción: "))
        den1 = float(input("Ingrese el denominador de la primera fracción: "))
        num2 = float(input("Ingrese el numerador de la segunda fracción: "))
        den2 = float(input("Ingrese el denominador de la segunda fracción: "))
        numerador = (num1 * den2) + (num2 * den1)
        denominador = den1 * den2
        resultado = (numerador, denominador)
        print("Resultado:", resultado)

    def salir(self):
        print("¡Hasta luego!")

    def mostrar_menu(self):
        print("\nOpciones disponibles:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Calcular promedio")
        print("6. Sumar fracciones homogéneas")
        print("7. Salir")

    def ejecutar_opcion(self, opcion):
        if opcion in self.opciones:
            self.opciones[opcion]()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

    def ejecutar_calculadora(self):
        print("¡Bienvenido a la calculadora científica multifuncional!")

        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción (1-7): ")
            self.ejecutar_opcion(opcion)

# Ejecutar la calculadora
calculadora = Calculadora()
calculadora.ejecutar_calculadora()
