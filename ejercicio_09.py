"""
Enrique S. Fernandez
Ejercicio 9:
Dadas las siguientes listas:
edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]
y considerando que la posición en la lista corresponde a la misma persona,
mostar el nombre de la persona más joven
"""
ages = [25,36,18,23,45]
names = ["Juan","Ana","Sol","Mario","Sonia"]
young_age = ages[0]
young_name = names[0]

youngest_one= {'name': '', 'age': 00}

for num in ages:
    if num < young_age:
        young_age=num

young_name = names[ages.index(min(ages))]

youngest_one['name'] = young_name
youngest_one['age'] = young_age

print(youngest_one['name']+" "+str(youngest_one['age']))