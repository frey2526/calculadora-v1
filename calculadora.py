import math
import os

ARCHIVO = os.path.join(os.path.dirname(__file__), "historial.txt")


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre 0"
    return a / b


def raiz_cuadrada(a):
    if a < 0:
        return "Error: no se puede sacar raíz de un número negativo"
    return math.sqrt(a)


def pedir_numero(mensaje):
    while True:
        texto = input(mensaje)
        try:
            return float(texto)
        except ValueError:
            print("Eso no es un número. Intenta de nuevo.")


def cargar_historial():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return [linea.strip() for linea in f]
    except FileNotFoundError:
        return []


def guardar_historial():
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        for item in historial:
            f.write(item + "\n")


historial = cargar_historial()

print("=== CALCULADORA ===")
print("+  sumar")
print("-  restar")
print("*  multiplicar")
print("/  dividir")
print("r  raíz cuadrada (ejemplo: r 9 = 3)")
print("historial  ver operaciones anteriores")
print("limpiar    borrar historial")
print("salir     terminar")

while True:
    operacion = input("\nOperación: ").strip()

    if operacion == "salir":
        print("¡Hasta luego!")
        break

    if operacion == "historial":
        if not historial:
            print("Aún no hay operaciones.")
        else:
            print("--- Historial ---")
            for item in historial:
                print("-", item)
        continue

    if operacion == "limpiar":
        historial.clear()
        guardar_historial()
        print("Historial borrado.")
        continue

    if operacion not in ("+", "-", "*", "/", "r"):
        print("Operación no válida. Mira el menú de arriba.")
        continue

    if operacion == "r":
        a = pedir_numero("Número: ")
        resultado = raiz_cuadrada(a)
        entrada = f"√ {a} = {resultado}"
    else:
        a = pedir_numero("Primer número: ")
        b = pedir_numero("Segundo número: ")

        if operacion == "+":
            resultado = sumar(a, b)
        elif operacion == "-":
            resultado = restar(a, b)
        elif operacion == "*":
            resultado = multiplicar(a, b)
        else:
            resultado = dividir(a, b)

        entrada = f"{a} {operacion} {b} = {resultado}"

    print("Resultado:", resultado)
    historial.append(entrada)
    guardar_historial()
