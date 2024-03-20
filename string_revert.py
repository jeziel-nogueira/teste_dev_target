my_string = input("Informe uma palavra ou frase para invertermos:")
new_string = ""

for letter in range(len(list(my_string))-1, -1, -1):
    new_string += list(my_string)[letter]
print(new_string)