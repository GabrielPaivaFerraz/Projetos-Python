# tecnico em informatica
#autor: Gabriel 
#data de inicio:08/02/2022
#data de termino:11/02/2022

import os

os.system('cls')

def monta_dicionario(lista1, lista2):

    dicionario = dict(zip(lista1, lista2))

    return dicionario

lista1 = ['nome', 'peso', 'idade']
lista2 = ['John', 40, 1.80]

print('-'*70)
print('Juntando lista em dicionario ')
print('='*70)

print(f'lista 1:', end=' ')
for intem in lista1:
    print(f'{intem}', end='\t')

print()
print(f'lista 2:', end=' ')
for item in lista2:
    print(f'{item}', end='\t')
print()
print('-'*70)

print()
print('Dincionario montado com lista 1 e 2')
print('='*70)

resultado = monta_dicionario(lista1, lista2)

for chave, valor in resultado.items():
    print(f'{chave}: {valor}', end='\t')
print()
print('-'*70)
print()    
