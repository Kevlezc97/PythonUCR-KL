""""Strings intercaladas: Escriba un programa que reciba dos strings del mismo
largo por parte del usuario e imprima una nueva string con los caracteres de
ambos inputs intercalados."""

a = input("Ingrese Primer Palabra:")
b = input ("Ingrese Segunda Palabra:")

result = [val for pair in zip(a, b) for val in pair]
print(result)
