""""Elimina repetidos: Crea un programa que elimine los elementos repetidos de una lista."""

my_list = [1,2,3,3,2,4,6]
eliminar = set (my_list)
output = []
for i in eliminar:
    output.append(i)
print(output)

my_list = [3,3,3,3,3,3,3]
eliminar = set (my_list)
output = []
for i in eliminar:
    output.append(i)
print(output)
