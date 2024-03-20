
# inverter a string informada
def invert_string(my_string):
    new_string = ""
    for letter in range(len(list(my_string))-1, -1, -1):
        new_string += list(my_string)[letter]
    print(new_string)

# loop para input da string
def main():
    while 1:
        check_input = input(" * Se deseja informar uma string digite 1;\n * Ou pressine enter para finalizar: \n")
        if check_input == '1':
            invert_string(input("Informe uma palavra ou frase para invertermos:\n"))
        else:
            break
        

if __name__ == "__main__":
    main()

