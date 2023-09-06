"""
Enrique S. Fernandez
Ejercicio 10:
Pedir al usuario que ingrese los datos de 5 alumnos y guardarlos en sus 
respectivas listas. Validar el ingreso de datos según su criterio.
Datos:
nombre, sexo (f/m), nota (validar).
Una vez cargados los datos:
Mostrar el nombre del hombre con nota más baja
Mostrar el promedio de notas de las mujeres

Ejemplo: 
nombres = ["Juan","Pedro","Sol","Paco","Ana"]
sexo = ["m","m","f","m","f"]
nota = [6,8,10,8,5]
"""
nombres = []
sexos = []
notas = []

for i in range(5):
    nombre = input('ingresa nombre del alumno')
    while nombre == "":
        nombre='ingrese un nombre valido'
    sexo = input('ingrese genero (f/m): ')
    while sexo !='f' and sexo !='m':
        sexo = input('ingrese f o m: ')
    nota = input('ingrese nota:')
    while not nota.isdigit:
        nota = input('debe ingresar una nota:')
    
    nota = int(nota)
    nombres.append(nombre)
    sexos.append(sexo)
    notas.append(nota)




print(nombres, sexos, notas)