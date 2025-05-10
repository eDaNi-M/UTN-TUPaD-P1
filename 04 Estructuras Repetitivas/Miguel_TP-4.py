#ACLARACION: LAS VARIABLES LAS DECLARO CON EL NUMERO CORRESPONDIENTE AL NUMERO DE ACTIVIDAD 
#PARA QUE NO HAYA MEZCLAS EN POSIBLES VARIABLES NOMBRADAS IGUALES EN DISTINTAS ACTIVIDADES.

# Ejercicio 1
for i in range(101):
    print(i)


# Ejercicio 2
numero2 = input("Introduce un número entero: ")
cantidad_digitos2 = len(numero2.lstrip('-'))

print(f"El número tiene {cantidad_digitos2} dígitos.")


# Ejercicio 3
inicio3 = int(input("Introduce el primer número: "))
fin3 = int(input("Introduce el segundo número: "))

suma3 = sum(range(inicio3 + 1, fin3))

print(f"La suma de los números entre {inicio3} y {fin3} es: {suma3}")


# Ejetotal4 = 0
while True:
    numero4 = int(input("Introduce un número (0 para terminar): "))
    if numero4 == 0:
        break

    total4 += numero4

print(f"El total acumulado es: {total4}")


# Ejercicio 5
import random

def adivinar_numero5():
    numero_secreto5 = random.randint(0, 9)
    intentos5 = 0
    adivinado5 = False

    while not adivinado5:
        intento5 = int(input("Adivina el número entre 0 y 9: "))
        intentos5 += 1
        if intento5 == numero_secreto5:
            adivinado5 = True

    print(f"¡Correcto! El número era {numero_secreto5}. Lo adivinaste en {intentos5} intentos.")

adivinar_numero5()


# Ejercicio 6
def pares_decreciente6():
    for i in range(100, -1, -1):
        if i % 2 == 0:
            print(i)

pares_decreciente6()


# Ejercicio 7
def suma_hasta_numero7():
    numero7 = int(input("Ingresa un número entero positivo: "))
    if numero7 < 0:
        print("El número debe ser positivo.")
        return

    suma7 = 0
    for i in range(numero7 + 1):
        suma7 += i

    print(f"La suma de los números entre 0 y {numero7} es: {suma7}")

suma_hasta_numero7()


# Ejercicio 8
def contar_numeros8():
    cantidad8 = 100
    pares8 = impares8 = positivos8 = negativos8 = 0

    for i in range(cantidad8):
        num8 = int(input(f"Ingrese el número {i+1}: "))
        if num8 % 2 == 0:
            pares8 += 1
        else:
            impares8 += 1
        if num8 >= 0:
            positivos8 += 1
        else:
            negativos8 += 1

    print(f"Pares: {pares8}")
    print(f"Impares: {impares8}")
    print(f"Positivos: {positivos8}")
    print(f"Negativos: {negativos8}")

contar_numeros8()


# Ejercicio 9
def calcular_media9():
    cantidad9 = 100 
    suma9 = 0

    for i in range(cantidad9):
        num9 = int(input(f"Ingrese el número {i+1}: "))
        suma9 += num9

    media9 = suma9 / cantidad9
    print(f"La media de los {cantidad9} números es: {media9}")

calcular_media9()


# Ejercicio 10
def invertir_digitos10():
    numero10 = input("Ingresa un número: ")
    invertido10 = numero10[::-1]
    print(f"El número invertido es: {invertido10}")

invertir_digitos10()
