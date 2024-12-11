#Paso 1: solicitar al usuario el radio del circulo
import math


radio = float(input("Por favor ingrese el radio del circulo que desea calcular "))

#Paso 2: Calcular el area del circulo
area = math.pi * (radio**2)

#Paso 3: Mostrar al usuario el area calculada
print("El area del circulo con radio ", radio, "es: ",area)