# FUNCIONES / MÓDULOS / PROCEDIMIENTOS / MÉTODOS / RUTINAS
# Son acciones o tareas a ejecutar (verbos en ar, er, ir)
# SINTAXIS:
'''
def Nombre_de_la_Función ( Argumentos o Parámetros ):
  contenido de la función
  return valor(es)
'''
import os
# Declarar las Funciones
def Sumar(num1, num2):  # Obtener o recibir los parámetros
  return num1 + num2    # Regresar, Devolver, Retornar un valor

def Restar(numero1, numero2):
  resta = numero1 - numero2
  print("La resta =", resta)


# Mandar a llamar o invocar las funciones
# Imprimir el resultado
respuesta = "si"
while (respuesta == "Si" or respuesta == "si" or respuesta == "Y" or respuesta == "y"):
  os.system("cls") # clear screen
  print("OPERACIONES MATEMÁTICAS")
  print("1) Suma\n2) Resta\n3) Mult\n4) División\n5) Salir")
  opción = int(input("Elige una operación: "))

  if (opción == 1):
    print("La suma =", Sumar(10, 5))  # Enviar o pasar los parámetros
  elif (opción == 2):
    Restar(50, 20)
  elif (opción == 5):
    print("Saliendo...")
    break
  else:
    print("Opció NO VÁLIDA")
  
  respuesta = input("¿Quieres continuar? (Si/No): ")
