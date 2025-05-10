#ACLARACION: LAS VARIABLES LAS DECLARO CON EL NUMERO CORRESPONDIENTE AL NUMERO DE ACTIVIDAD 
#PARA QUE NO HAYA MEZCLAS EN POSIBLES VARIABLES NOMBRADAS IGUALES EN DISTINTAS ACTIVIDADES.

# Ejercicio 1
multiplosDe4_1 = list(range(4, 101, 4))
print(multiplosDe4_1)


# Ejercicio 2
mis_elementos2 = ["pizza", "pc", "futbol", "guitarra", "viajes"]
print(mis_elementos2[-2])


# Ejercicio 3
lista_vacia3 = []
lista_vacia3.append("boca")
lista_vacia3.append("casa")
lista_vacia3.append("universo")
print(lista_vacia3)


# Ejercicio 4
animales4 = ["perro", "gato", "vaca", "pez"]
animales4[1] = "leon"
animales4[-1] = "oso"
print(animales4)


# Ejercicio 5
numeros5 = [8,15,3,22,7]
numeros5.remove(max(numeros5))

print(numeros5)

#Lo que sucede en este ejercicio es que tenemos una variable llamada numeros-
#que contiene una lista de numeros.
#Siguiendo con el ejercicio enctramos el metodo remove que remueve un elemento de la lista-
#que lo complementamos con la funcion max que en este caso identifica el numero mas alto-
#de la lista y y poceden conjuntamente a eliminar ese numero de la lista.
#Como paso final imprime la lista ya modificada.

# Ejercicio 6
numeros6 = list(range(10, 31, 5))
print(numeros6[:2])


# Ejercicio 7
autos7 = ["sedan", "polo", "suran", "gol"]
autos7[1] = "corolla"
autos7[2] = "etios" 
print(autos7)


# Ejercicio 8
dobles8 = []
dobles8.append(5 * 2)
dobles8.append(10 * 2)
dobles8.append(15 * 2)
print(dobles8)


# Ejercicio 9
compras9 = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras9[2].append("jugo")
compras9[1][1] = "tallarines"
compras9[0].remove("pan")

print(compras9)


# Ejercicio 10
lista_anidada10 = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
print(lista_anidada10)
