# tecnico em informatica
#autor: Gabriel 
#data de inicio:07/02/2022
#data de termino:07/02/2022


import os 

os.system('cls')


def divisao(a, b):
    try:
        d = a / b
        return d 
    except ZeroDivisionError:
        return 'ERRO! nao podemos dividir um numero por zero! '

a = 10 
b = 0 

#calculando a divisao
resultado = divisao(a, b)

#saida
print('-'*70)
print(f'O numero {a} / {b} = {resultado}')
print('-'*70)
print()

