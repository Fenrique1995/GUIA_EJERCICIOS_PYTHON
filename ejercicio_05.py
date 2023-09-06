"""
Enrique S. Fernandez
Ejercicio 5:
Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000 
por cada estadía como base, se pide el ingreso de una estación del 
año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del 
Plata/Córdoba) para vacacionar para poder calcular el precio final:
-en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un 
descuento del 10% Mar del Plata tiene un descuento del 20%
-en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene 
un aumento del 10% Mar del Plata tiene un aumento del 20%
-en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un 
aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el 
precio sin descuento.
Validar el ingreso de datos
"""

tarifa = 15000
estacion_del_año = ['invierno','verano','otoño','primavera']


destino = int(input('ingrese su destino \n 1)bariloche \n 2)cataratas \n 3)mar del plata \n 4)córdoba \n'))
while destino < 0 or destino > 4:
    destino = int(input('debe ingresar una de estas opciones \n 1)bariloche \n 2)cataratas \n 3)mar del plata \n 4)córdoba \n'))

estacion = input('ingrese la estacion del año en la que se encuentra (invierno/verano/otoño/primavera)')

while estacion != estacion_del_año[0] and estacion != estacion_del_año[1] and estacion != estacion_del_año[2] and estacion != estacion_del_año[3]:
    estacion = input('ingrese una de las estaciones tal se encuentra aqui (invierno/verano/otoño/primavera)')

match destino:
    case 1:
        if estacion == estacion_del_año[0]:
            tarifa *= 1.2
            print('Su tarifa es de: '+str(tarifa))
        elif estacion ==  estacion_del_año[1]:
            tarifa /= 1.2
            print('Su tarifa es de: '+str(tarifa))
        else:
            tarifa *= 1.1
            print('Su tarifa es de: '+str(tarifa))
    case 2:
        if estacion == estacion_del_año[0]:
            tarifa /= 1.1
            print('Su tarifa es de: '+str(tarifa))
        else:
            tarifa *= 1.1
            print('Su tarifa es de: '+str(tarifa))
    case 3:
        if estacion == estacion_del_año[0]:
            tarifa /= 1.2
            print('Su tarifa es de: '+str(tarifa))
        elif estacion ==  estacion_del_año[1]:
            tarifa *= 1.2
            print('Su tarifa es de: '+str(tarifa))
        else:
            tarifa *= 1.1
            print('Su tarifa es de: '+str(tarifa))
    case 4:
        if estacion == estacion_del_año[0]:
            tarifa /= 1.1
            print('Su tarifa es de: '+str(tarifa))
        elif estacion ==  estacion_del_año[1]:
            tarifa *= 1.1
            print('Su tarifa es de: '+str(tarifa))
        else:
            tarifa 
            print('Su tarifa es de: '+str(tarifa))