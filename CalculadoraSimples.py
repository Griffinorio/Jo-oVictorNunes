print('\033[1;36m-=\033[m' * 20)
print('             \033[4;34mCALCULADORA\033[m')
print('\033[1;36m-=\033[m' * 20)



num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

print('''
Escolha uma das operações a seguir: 
\033[4;34m[1] ADIÇÃO (+)\033[m
\033[4;34m[2] SUBTRAÇÃO (-)\033[m
\033[4;34m[3] MULTIPLICAÇÃO (x)\033[m
\033[4;34m[4] DIVISÃO (/)\033[m
      ''')
opcao = int(input('Digite sua opção: '))

if opcao == 1:
    print('{} + {} = \033[4;36m{}\033[m'.format(num1, num2, num1 + num2))
elif opcao == 2:
    print('{} - {} = \033[4;36m{}\033[m'.format(num1, num2, num1 - num2))
elif opcao == 3:
    print('{} x {} = \033[4;36m{}\033[m'.format(num1, num2, num1 * num2))
elif opcao == 4:
    if num2 == 0:
        print('Não é possível dividir por 0 (zero)')
    else:
        print('{} / {} = \033[4;36m{}\033[m'.format(num1, num2, num1 / num2))
else:
    print('Operação Inválida!')



