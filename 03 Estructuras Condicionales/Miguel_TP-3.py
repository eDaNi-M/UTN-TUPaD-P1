# Informacio: EN LAS VARIABLES UTILIZO LA NUMERACION DE LA ACTIVIDAD PARA QUE NO SE MEZCLEN ENTRE LAS VARIABLES DE LAS OTRAS ACTIVIDADES


# Ejercicio 1
edad1 = int(input("ingrese su edad"))

if edad1 > 18 :
    print ("Eres mayor de edad")
else:
    print("intentalo de nuevo en unos años")


# Ejercicio 2
nota = float(input("Ingrese su nota"))

if nota >= 6:
    print ("Aprobado")
else:
    print ("Desaprobaste mi rey, mejor suerte la proxima")


# Ejercicio 3
numeroPar = int(input("Ingrese un numero par"))

if numeroPar % 2 == 0:
    print("es un numero par")
else:
    print("Por favor, Ingrese un numero par")


# Ejercicio 4
edad4 = int(input("Ingrese su edad"))

if edad4 < 12:
    print("Eres un niño")
elif edad4 >= 12 and edad4 < 18:
    print ("Eres un adolescente")
elif edad4 >= 18 and edad4 <30:
    print("Eres un adulto joven")
else:
    print("Eres un adulto")


# Ejercicio 5
contraseña = input("Introducir Contraseña de entre 8 y 14 caracteres")

if len(contraseña) >= 8 and len(contraseña) <=14:   
    print("Has ingresado una contraseña correcta")
else:
    print("Ingrese una contraseña de entre 8 y 14 caracteres")


# Ejercicio 7
texto7 = input("Ingrese una frase o palabra: ")

if texto7[-1].lower() in "aeiou":
    texto7 += "!"  

print("Resultado:", texto7)



# Ejercicio 8
nombre8 = input("Ingrese su nombre: ")
opcion8 = input("Elija una opción (1: mayúsculas, 2: minúsculas, 3: primera letra mayúscula): ")

if opcion8 == "1":
    print(nombre8.upper())
elif opcion8 == "2":
    print(nombre8.lower())
elif opcion8 == "3":
    print(nombre8.title())
else:
    print("Opción no válida.")


# Ejercicio 9
magnitud9 = float(input("Ingrese la magnitud del terremoto: "))

if magnitud9 < 3:
    print("Muy leve (imperceptible)")
elif magnitud9 < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud9 < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud9 < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud9 < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")


# Ejercicio 10
hemisferio10 = input("¿En qué hemisferio estás? (N/S): ").upper()
mes10 = int(input("¿En qué mes estamos? (1-12): "))
dia10 = int(input("¿Qué día del mes es hoy? (1-31): "))

dias_por_mes10 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if not (1 <= mes10 <= 12 and 1 <= dia10 <= dias_por_mes10[mes10 - 1]):
    print("Fecha inválida.")
else:
    dia_del_año10 = sum(dias_por_mes10[:mes10 - 1]) + dia10

    if 355 <= dia_del_año10 or dia_del_año10 <= 79:
        estacion_norte10 = "Invierno"
        estacion_sur10 = "Verano"
    elif 80 <= dia_del_año10 <= 171:
        estacion_norte10 = "Primavera"
        estacion_sur10 = "Otoño"
    elif 172 <= dia_del_año10 <= 263:
        estacion_norte10 = "Verano"
        estacion_sur10 = "Invierno"
    else:
        estacion_norte10 = "Otoño"
        estacion_sur10 = "Primavera"


    if hemisferio10 == "N":
        print(f"Estás en el hemisferio norte. La estación es: {estacion_norte10}.")
    elif hemisferio10 == "S":
        print(f"Estás en el hemisferio sur. La estación es: {estacion_sur10}.")
    else:
        print("Hemisferio inválido.")

