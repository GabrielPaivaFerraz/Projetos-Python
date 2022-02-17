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
nomes = ()

#COnvertendo a tupla em lista 
listaNomes = list(nomes)

#Entrada de dados 
for c in range(0, 4, 1):
    listaNomes.append(str(input('Digite o nome: ')))

#Convertendo a lista em tupla 
nomes = tuple(listaNomes)

#saida
print('Nomes: \t', end=' ')
for indice,nome in enumerate(nomes):
    print(f'{indice} : {nome}', end=' ')
print()

print('-'*80)
print()

nome = str(input('Digite um nome para remover da tupla: '))
if(nome not in nomes):
    print('Nome nao esta na tupla!')
else:
    #Convertendo a tupla em lista 
    listaNomes = list(nomes) 
    listaNomes.remove(nome) 

    #Convertendo a lista em tupla 
    nomes = tuple(listaNomes)

#saida
print('Nomes: \t', end=' ')
for indice, nome in enumerate(nomes):
    print(f'{indice} : {nome}', end=' ')
print()
print('-'*80) 
print()
    
