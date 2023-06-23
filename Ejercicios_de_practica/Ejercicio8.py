# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un
# cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el
# cociente y el resto de la división entera respectivamente.

num1 = int(input('Ingresa el primer numero:'))
num2 = int(input('Ingresa tu segundo numero:'))
division = (num1/num2)
resto = (num1 % num2)
print('Tu numero 1 entre tu numero 2 da un cociente de:',
      str(division), 'y un resto', str(resto))
