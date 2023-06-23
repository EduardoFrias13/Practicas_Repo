"""Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
y muestre por pantalla el capital obtenido en la inversión."""

cant_inver = float(input('Ingrese la cantidad a invertir:'))
int_anual = float(input('Ingrese el interes anual:'))
años = int(input('Ingrese los años:'))

print('Capital obtenido:', str(round(cant_inver * (int_anual / 100 + 1) ** años, 2)))
