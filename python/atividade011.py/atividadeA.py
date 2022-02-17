# tecnico em informatica
#autor: Gabriel 
#data de inicio:7/12/2021
#data de termino:/12/2021

import os

os.system('cls')


def lista_numeros(lista):
    pares = []
    impares = []
    quantidade_pares = 0
    quantidade_impares = 0

    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
            quantidade_pares += 1

        else:
            impares.append(numero)
            quantidade_impares += 1
    return pares, impares, quantidade_pares, quantidade_impares

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]   

num_pares, num_impares, quant_pares, quant_impares = lista_numeros(lista)


print('-'*70)
print('lista completa: ', end=' ' )
for numero in lista:
    print(numero, end=' ')
print()
print('='*70)

print(f'lista pares: ',end=' ')
for numero in num_pares:
    print(numero, end=' ')

print()

print(f'lista impares: ', end=' ')
for numero in num_impares:
    print(numero, end=' ')

print()

print(f'Quantidade de numeros pares: {quant_pares}')
print(f'Quantidade de numeros impares: {quant_impares}')
print('-'*70)