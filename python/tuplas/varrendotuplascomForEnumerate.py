# tecnico em informatica
#autor: Gabriel 
#data de inicio:1/11/2021
#data de termino:1/11/2021


import os
os.system('cls')

print('-'*80)
print('Verificaçao in e not in')
print('='*80)

#Declaraçao
numeros = (1, 2, 3, 4, 5, 6) #Interios
atores = ('Norma Reedus', 'Melissa McBride' , 'Lauren Cohan') #Strings
personagens =('Daryl Dixon', 'Carol Peletier', 'Maggie Rhee') #Strings
decimais = (1.2, 3.4, 5.6, 7.8) # Ponto flutuante
mix = ('John', 40, 1.77, True)

#saida
print('Numeros: \t', end= ' ')
for indice, numero  in enumerate(numeros):
    print(f'{indice} : {numero}', end=' ')
print()

print('Atores: \t', end=' ')
for indice,ator in enumerate(atores):
    print(f'{indice} : {ator}', end=' ')
print()

print('Personagens: \t', end=' ')
for indice,personagem in enumerate(personagens):
    print(f'{indice} : {personagem}', end=' ')
print()

print('Decimais \t', end=' ')
for indice, decimal in enumerate(decimais):
    print(f' {indice} : {decimal}', end=' ')
print()

print('miscelanea: \t', end=' ')
for indice, item in enumerate(mix):
    print(f'{indice} : {item}', end=' ')
print()

print('-'*80)
print()
