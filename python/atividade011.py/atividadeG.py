# tecnico em informatica
#autor: Gabriel 
#data de inicio:08/02/2022
#data de termino:11/02/2022


print('''
         1. soma
         2. subtraçao
         3. produto
         4. divisao
         5.divisao inteira
         6. resto da divisao
         7. sair
         ''')



import os
os.system('cls')

def calculos(numero1, numero2, escolha):
    if escolha == 1:
        soma= numero1 + numero2
        return '+', soma

    elif escolha == 2:
        subtraçao = numero1 - numero2
        return '-', subtraçao
            
    elif escolha == 3:
        produto = numero1 * numero2
        return 'x', produto

    elif escolha == 4:
        if numero2 == 0:
            return '/', 'Impossivel dividir por zero! '
        else:
            divisao = numero1 / numero2
            return '/', divisao

    elif escolha == 5:
        if numero2 == 0:
            return '//', 'impossivel dividir por zero! '

    elif escolha == 6:
        if numero2 == 0:
            return '%', 'Impossivel dividir por zero! '
        else:
            resto_divisao = numero1 % numero2
            return '%', resto_divisao

while True:

    print('''
         1. soma
         2. subtraçao
         3. produto
         4. divisao
         5.divisao inteira
         6. resto da divisao
         7. sair
         ''')

    try:
        escolha = int(input('Escolha uma operaçao (1-7): '))

        if escolha == 7:
            break

        else:
            numero1 = float(input('Entre com o 1° numero: '))
            numero2 = float(input('Entre com o 2° numero: ')) 

            operador, resultado = calculos(numero1, numero2, escolha)

            print('-'*70)
            print(f'O resultado de' +
                   f' {numero1} { operador} {numero2} e igual a: {resultado}')
            print('-'*70)
            print()

    except (ValueError, TypeError):
        print('Valor invalido! ')                  