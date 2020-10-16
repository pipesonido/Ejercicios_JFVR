#Dado los valores ingresados por el usuario (base,altuta) calcular y mostrar en pantalla el área del triangulo
# base = float(input("Ingrese la base del triangulo: "))
# altura = float(input("Ingrese la la altura del triangulo: "))
# area = (base*altura)/2
# print("El área del triangulo es: " , area)

#Convertir la cantidad de dolares ingresado por un usuario a pesos colombianos y mostrar el resultado en pantalla
# dolares = int(input("Ingrese la cantidad de dolares a convertir: "))
# COP = dolares*3850
# print("El valor en pesos es: " , COP)

#Convertir los grados centigrados ingresados por  un usuario a grados Farenheit y mostrar el resultado en pantalla
# GradosC = float(input("Ingrese la la temperatura en ºC: "))
# GradosF = GradosC*9/5
# print("El área del triangulo es: " , GradosF)

#Mostrar en pantalla la cantidad de segundos que tiene un lustro
# lustro = 5*365*24*60*60
# print("La cantidad de segundos que tiene un lustro son:" , lustro)

#Calcular la cantidad de segundos que le toma a la luz viajar del sol a Marte y mostrar el resultado en pantalla
# VelLuz = 299792
# Dist = 227388762
# SegSolMarte = Dist/VelLuz
# print("La cantidad de segundos que le toma a la luz viajar del sol a Marte son" , SegSolMarte , "segundos")

#Calcular el numero de vueltas que da una llanta en 1km, dado que el diametro de la llanta es de 50cm, mostrar el resultado en pantalla
# import math
# pi = math.pi
# Diametro = 50
# Longitud = 2*pi*(Diametro/2)
# NumVueltas = int( 100000/Longitud)
# print("El numero de vueltas que da una llanta en 1km son: " , NumVueltas , "vueltas")

#Calcular y mostrar en pantalla la longitud de la sombra de un edificio de 20 metros de altura cuando el angulo que forman los rayos del sol con el suelo es de 22º
# import math
# CatOpuesto = 20
# alfaDeg = 22
# alfaRad = math.radians(alfaDeg)
# catAdy = CatOpuesto / math.tan(alfaRad)
# print("la longitud de la sombra de un edificio de 20 metros de altura es" , catAdy , "metros")

#Mostrar en pantalla TRUE o FALSE si la edad ingresada por dos usuarios es la misma
# EdadU1 = int(input("Ingrese la edad del usuario 1: "))
# EdadU2 = int(input("Ingrese la edad del usuario 2: "))
# if EdadU1 == EdadU2:
#     print("Las edades son iguales")
# else:
#     print("Las edades son diferentes")

#Mostrar en pantalla la cantidad de meses transcurridos desde la fecha de nacimiento de un usuario
# import datetime
# from datetime import timedelta

# while True:
#     try:
#         fecha = input("Ingrese la fecha de nacimiento con el formato DD/MM/YYYY ")
#         fecha = datetime.datetime.strptime(fecha,"%d/%m/%Y")
#         today = datetime.date.today()
#         hoy = datetime.datetime.now()
#         difer = hoy - fecha
#         break
#     except ValueError:
#         print("El formato debe ser DD/MM/YYYY")

# print ("Los meses transcurridos desde su nacimiento son ", int(difer.days / 30))

#Mostrar en pantalla el promedio de un alumno que ha cursado 5 materias (Español, Matemáticas, Economía, Programación, Ingles)
# Esp = float(input("Ingrese la nota de Español "))
# Mat = float(input("Ingrese la nota de Matemáticas "))
# Econ = float(input("Ingrese la nota de Economía "))
# Prog = float(input("Ingrese la nota de Programación "))
# Ing = float(input("Ingrese la nota de Ingles "))
# PromNotas = (Esp+Mat+Econ+Prog+Ing)/5
# print("El promedio de notas es: " , PromNotas)