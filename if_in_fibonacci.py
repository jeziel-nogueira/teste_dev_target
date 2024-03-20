import random


def check_number_exist(num):    
    value_b = 1
    value_A, sum = 0, 0

    while sum <= num:
        sum = value_A + value_b
        if sum == num:
            break
        value_A = value_b
        value_b = sum

    if sum == num:
        print(f'O valor {num} pertence a sequência de Fibonacci')
    else:
        print(f'O valor {num} não pertence a sequência de Fibonacci')


def main():
    while 1:
        check_input = input(" * Se deseja informar um valor digite 1;\n * Pressione enter para um número aleatório \n * Ou informe 2 para finalizar: \n")
        if check_input == '1':
            check_number_exist(int(input("informe o valor: ")))
        elif check_input == '2':
            break
        else:
            value_to_check = random.randint(0, 100)
            print(f'Valor randômico: ', value_to_check)
            check_number_exist(value_to_check)
        

if __name__ == "__main__":
    main()

