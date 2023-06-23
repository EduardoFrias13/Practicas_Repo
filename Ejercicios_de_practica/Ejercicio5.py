# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
# Después debe mostrar por pantalla la paga que le corresponde.

horas_trabajadas = float(input('Ingresa las horas que trabajaste:'))
costo_horas = float(input('Ingresa tu precio por hora trabajada:'))
print('Tu pago es de:', (horas_trabajadas*costo_horas), 'pesos')
