"""
Enrique S. Fernandez
Ejercicio 4:
Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil 
distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO 
ser soltero.'
"""
estados_civiles = ['soltero', 'casado', 'divorciado', 'viudo']
edad = int(input('ingrese edad: '))
estado_civil = input('ingrese estado civil (soltero/casado/divorciado/viudo): ')
while estado_civil != estados_civiles[0] and estado_civil != estados_civiles[1] and estado_civil != estados_civiles[2] and estado_civil != estados_civiles[3]:
    estado_civil = input('debe ingresar una de estas cuatro opciones (soltero/casado/divorciado/viudo): ')

if edad < 18 and estado_civil != estados_civiles[0]:
    print('Es muy pequeño para NO ser soltero.')
else:
    print('Todo bien')