import random

value_b = 1

sum, value_A, value_to_check = 0, 0, 0

check_input = input("Se deseja informar um valor digite 1;\n ou pressione enter para um número aleatório: ")
if check_input == '1':
    value_to_check = int(input("informe o valor: "))
else:
    value_to_check = random.randint(0, 100)
    print(f'Valor randômico: ', value_to_check)

while sum <= value_to_check:
    sum = value_A + value_b
    if sum == value_to_check:
        break
    value_A = value_b
    value_b = sum


if sum == value_to_check:
    print(f'O valor {value_to_check} pertence a sequência de Fibonacci')
else:
    print(f'O valor {value_to_check} não pertence a sequência de Fibonacci')