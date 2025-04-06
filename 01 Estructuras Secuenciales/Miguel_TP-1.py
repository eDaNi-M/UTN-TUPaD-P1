# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola mundo")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

nombre = input ("Ingrse su nombre")
print (f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

nombretres = input("Ingrese su nombre")
apellidotres = input("Ingrese su apellido")
edadtres = input("Ingrese su edad")
localidadtres = input("Ingrese su pais de residencia")
print(f"Soy {nombretres} {apellidotres}, tengo {edadtres} anios y vivo en {localidadtres}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.
# Pedir al usuario el radio

radio = float(input("Introduce el radio del círculo: "))
pi = 3.1416
area = pi * radio ** 2
perimetro = 2 * pi * radio
print("Área del círculo:", area)
print("Perímetro del círculo:", perimetro)


# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

segundos = input("Ingrese la cantidad de segundo")
segundos = int(segundos)
hora = int(3600)
resultado= segundos / hora
print (f"La cantidad de horas es de: {resultado}")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

numeroseis = int(input("Introduce un número: "))
print(numeroseis, "x 1 =", numeroseis * 1)
print(numeroseis, "x 2 =", numeroseis * 2)
print(numeroseis, "x 3 =", numeroseis * 3)
print(numeroseis, "x 4 =", numeroseis * 4)
print(numeroseis, "x 5 =", numeroseis * 5)
print(numeroseis, "x 6 =", numeroseis * 6)
print(numeroseis, "x 7 =", numeroseis * 7)
print(numeroseis, "x 8 =", numeroseis * 8)
print(numeroseis, "x 9 =", numeroseis * 9)
print(numeroseis, "x 10 =", numeroseis * 10)

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

primerNumero = int(input("Ingrese el primer numero"))
segundoNumero = int(input("Ingrese el segundo numero"))
print (f"El resultado de sumar {primerNumero} y {segundoNumero} es:", primerNumero + segundoNumero)
print (f"El resultado de restar {primerNumero} y {segundoNumero} es:", primerNumero - segundoNumero)
print (f"El resultado de multiplicar {primerNumero} y {segundoNumero} es:", primerNumero * segundoNumero)
print (f"El resultado de dividir {primerNumero} y {segundoNumero} es:", primerNumero // segundoNumero)

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo:

peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))
imc = peso / (altura ** 2)
print(f"Tu índice de masa corporal (IMC) es: {imc}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

celsius = float(input("Introduce la temperatura en grados Celsius: "))
fahrenheit = (9 / 5) * celsius + 32
print(f"La temperatura en Fahrenheit es: {fahrenheit}")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

primnumero = float(input("Ingrese el primer numero (del 0 al 10)"))
segnumero = float(input("Ingrese el segundo numero (del 0 al 10)"))
ternumero = float(input("Ingrese el tercer numero (del 0 al 10)"))
promedio = (primnumero + segnumero + ternumero) / 3
print (f"Su promedio es de:{promedio}")
