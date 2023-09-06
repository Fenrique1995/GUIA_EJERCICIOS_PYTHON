"""
Enrique S. Fernandez
Ejercicio 8:
Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
mostrar el número repetido
"""
list = [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
watcher = set()
geminis = []

for num in list:
    if num in watcher:
        geminis.append(num)
    else:
        watcher.add(num)



print(geminis)