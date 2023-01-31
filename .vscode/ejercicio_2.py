""" Triángulo: Escriba un programa que reciba un número del usuario y
despliegue en pantalla el siguiente patrón de números llegando hasta el número elegido:"""


filas = int(input('Ingrese el número'))

for i in range(1, filas + 1):
    for f in range(1, i + 1):
        print(f, end=' ')
    print('')
