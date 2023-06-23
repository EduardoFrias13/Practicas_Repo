"""Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final
de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en
la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla
la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales."""

dinero_depositado = float(input('Ingresa la cantidad a depositar:'))
interes = 0.04

primer_año = dinero_depositado * (1 + interes)
print('La cantidad de ahorros tras el primer año es de:', str(round(primer_año, 2)))

segundo_año = primer_año * (1 + interes)
print('La cantidad de ahorros tras el segundo año es de:', str(round(segundo_año, 2)))

tercer_año = segundo_año * (1 + interes)
print('La cantidad de ahorros tras el tercer año es de:', str(round(tercer_año, 2)))
