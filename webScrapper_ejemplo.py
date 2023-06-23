import re
import requests

sitioweb = 'https://www.vulnhub.com/'
resultado = requests.get(sitioweb)
contenido = resultado.text
print(contenido)

patron = r'/entry/[\w-]*'
cosas_repetidas = re.findall(patron, str(contenido))
sin_duplicados = list(set(cosas_repetidas))

maquinas_final = []

for i in sin_duplicados:
    nombre = i.replace('/entry', '')
    maquinas_final.append(nombre)
    print(nombre)
