# -*- encoding: iso-8859-1 -*-
import sys
import io
import module1
from coche import coche


# Declaración de variables
nombre = "Alberto"
edad = 34
lugarNacimiento = "Sevilla"

# Imprimimos por pantalla
print ("Hola soy",nombre,"y tengo",edad,"años y nací en",lugarNacimiento)

# Creamos un coche
cocheAlberto = coche ("Seat", "Ateca", "negro", 20171101)
print (cocheAlberto.marca, cocheAlberto.color)