"""Lista al cubo: Escriba un programa que cree una lista de números y la
imprima. Luego debe imprimir dicha lista pero con cada valor convertido en
su cubo."""


lista_1 = [1, 2, 3]
lista_2 = []
print("La lista original es:")
print(lista_1)
print("La Lista vacía es:")
print(lista_2)
resultado = []
for i in lista_1:
    resultado.append(i*i*i)
print("La Lista al cubo es:")
print(resultado)
print("La lista vacía no tiene valor al cubo.")
