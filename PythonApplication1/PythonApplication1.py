# -*- encoding: iso-8859-1 -*-
import sys
import io
import module1
from coche import coche

# Creamos un coche
cocheAlberto = coche ("Seat", "Ateca", "negro", 2017)

# Declaración de variables
nombre = "Alberto"
edad = 34
lugarNacimiento = "Sevilla"


# Imprimimos por pantalla
print ("Hola soy",nombre,"y tengo",edad,"años y nací en",lugarNacimiento,". Tengo un coche que es un",cocheAlberto.marca,cocheAlberto.modelo,"del año",cocheAlberto.fechaMatriculacion)

