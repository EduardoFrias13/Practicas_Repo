# Escribir un programa que lea un entero positivo introducido por el usuario y después muestre en
# pantalla la suma de todos los enteros desde 1 hasta el numero introducido. La suma de los primeros
# enteros positivos puede ser calculada de la siguiente forma:

numero = int(input('Ingresa un numero:'))
suma = (numero*(numero+1)/2)
print('La suma desde 1 hasta', str(numero), 'es:', str(suma))
