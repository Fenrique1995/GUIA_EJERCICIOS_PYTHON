"""
Enrique S. Fernandez
Ejercicio 2:
Pedir una edad. Informar si la persona es mayor de edad (más de 18 años), 
adolescente (entre 13 y 17 años) o niño (menor a 13 años).
"""
edad = int(input('Ingrese edad: '))

if edad < 13:
    print('la persona es niño')
elif edad >= 18:
    print('la persona es mayor de edad')
else:
    print('la persona es adolscente')