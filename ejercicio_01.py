"""
Enrique S. Fernandez
Ejercicio 1:
Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su 
sueldo para esa persona.
"""

name = input("Nombre: ")
paid = int(input("Sueldo: "))
plus= int(paid * 1.10)

print(name+" "+str(plus))