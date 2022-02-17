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

#Condicional
#pode testar com not in
if(3 in numeros and 'Maggie Rhee' in personagens):
    resposta = 'Estao contidos em numeros e personagens.'
else:
    resposta = 'Nao estao contidos em numeros e personagens.'    

if('Maria' not in atores and 1.10 not in decimais):
    resposta2 = 'Nao estao contidos em atores e decimais.'
else:
    resposta2 = 'Estao contidos em atores e decimais.'

#saida
print(f'Verificaçao 1 :{resposta}\n ')
print(f'Verificaçao 2 :{resposta2}\n')
print('-'*80)
print()        