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
print('numeros:', end=' ')
for numero in numeros:
    print(numero, end=' ') 
print()

print('Atores: ', end=' ')
for atorAtriz in atores:
    print(atorAtriz, end =' ')
print()

print('Personagens: ', end=' ')
for personagem in personagens:
    print(personagem, end=' ')
print()

print('Decimais: ', end=' ')
for decimal in decimais:
    print(decimal, end=' ')
print()

print('Miscelanea: ', end=' ' )
for mix in mix:
    print(mix, end=' ')
print()

print('-'*80)
print()