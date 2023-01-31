""" Factorial del número dado: Escriba un programa en el que dado un número por el usuario,
# imprima el factorial (!) de dicho número.
# Verificar si el número es mayor a 0 """

num = int(input("Ingrese un Número: "))

FACTORIAL = 1

# check if the number is negative, positive or zero
if num < 0:
    print("Los Factoriales no son aplicables para números negativos")
elif num == 0:
    print("El Factorial de 0 es igual a 1")
else:
    for i in range(1,num + 1):
        FACTORIAL = FACTORIAL*i
    print("El Factorial del número",num,"corresponde a",FACTORIAL)
