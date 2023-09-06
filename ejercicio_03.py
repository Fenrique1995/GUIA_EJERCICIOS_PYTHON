"""
Enrique S. Fernandez
Ejercicio 3:
Ingresar 5 números enteros, distintos de cero. 
Informar:
a. Cantidad de pares e impares.
b. El menor número ingresado.
c. De los pares el mayor número ingresado.
d. Suma de los positivos.
e. Producto de los negativos
"""
counter = 0
counter_pairs = 0
counter_impairs = 0
flag = False
num_menor = 0
par_mayor = 0
flag_positive = False
suma_de_positivos = 0
producto_de_negativos = 0

while counter < 5:
    num = int(input('ingrese un numero distinto a 0: '))
    while num == 0:
        num = int(input('debe ingrese un numero distinto a 0: '))
    counter += 1

    if flag == False:
        flag = True
        num_menor = num
    if num < num_menor:
        num_menor = num

    if num % 2 == 0:
        counter_pairs += 1
        flag_positive = True
        par_mayor = num
        if num > par_mayor:
            par_mayor = num
            flag_positive = False
    else:
        counter_impairs += 1

    if num > 0:
        suma_de_positivos += num
    else:
        producto_de_negativos = -1 * num 

#a. Cantidad de pares e impares.
print("numeros pares: "+str(counter_pairs)+" numero impares: "+str(counter_impairs))
#b. El menor número ingresado.
print("numeros menor ingresado: "+str(num_menor))
#c. De los pares el mayor número ingresado.
print("El mayor de los pares: "+str(par_mayor))
#d. Suma de los positivos.
print("Suma de los positivos: "+str(suma_de_positivos))
#e. Producto de los negativos
print("Producto de los negativos: "+str(producto_de_negativos))