# Arreglos (Listas)
# Son variables para coleccionar o almacenar uno o más valores
# de uno o más tipos de datos
# SINTAXIS
'''
  arreglo_lista = [elementos/valores]
'''

# Declarar o crear un arreglo
nombres     =       ["Angélica", "Nicolás", "Emmanuel", "Rodolfo"]
# Índice (index)        0             1          2          3
edades      =       [26, 18, 22, 17]
# Índice (index)      0   1   2   3
arreglo_lista   =   [5, 6.8, "Hola", True]
# Índice (index)     0   1     2       3

# OPERACIONES CON ARREGLOS O LISTAS
# Modificar un elemento del arreglo
nombres[2] = "Emmanuel Adrián"
edades[3] = 21

# Agregar un elemento al último del arreglo
nombres.append("Eduardo")
edades.append(30)
arreglo_lista.append(False)

# Eliminar un elemento del arreglo
# nombres.pop(1)
# edades.pop(1)
arreglo_lista.pop(3)

# Vaciar el arreglo
# nombres.clear()
# edades.clear()
# arreglo_lista.clear()

# # Ordenar el arreglo por valores
nombres.sort() # Ordenamiento ASC
edades.sort(reverse = True) # Ordenamiento DESC

# Ordenar el arreglo por ubicación
nombres.reverse() # Ordenamiento DESC
edades.reverse()

# SALIDA DE DATOS
print("Nombres: ", nombres)
print("Edades: ", edades)
print("Arreglo: ", arreglo_lista)

datos_persona = ["nombre", 20, "@ipn.mx"]

# arreglo_objetos (JSON) Data Frames
lista_diccionarios = [
  { "nombre": "Angélica", "edad": 20, "correo": "" },
  { "nombre": "Nivolás", "edad": 18, "correo": "" },
]
