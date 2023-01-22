# - Problema 1

# Se necesita crear un programa que reciba del usuario una frase y decida si esa frase es un palíndromo o no. Un palíndromo se puede leer de igual forma de
# izquierda a derecha, que de derecha a izquierda. Ejemplo: "Anita lava la tina" 


word = input('phrase')
if (str(word) == str(word) [::-1]):
    print("Yes, the phrase is a Palindrome")
else:
    print("No, that phrase is not a Palindrome")
    #Anitalavalatina doesn't work, it works with Madam
    