# tecnico em informatica
#autor: Gabriel 
#data de inicio:1/11/2021
#data de termino:1/11/2021


import os
os.system('cls')

print('-'*80)
print('Declarando sets')
print('='*80)

#Declaraçao
nomes = {'John', 'Jane', 'Carol'}
numeros = {1, 2, 3, 4, 5, 6, 7}

#print(nomes[0]) #erron set nao tem indice

#mas posso varrer com for 
for nome in nomes:
    print(nome, end=' ')


print()    
print() 
print() 
print('-'*80)
print('Adicionando elemento nos sets')
print('-'*80)
#numeros.append() # erro , nao tem funçao append para sets

#metodo add() inserindo intes
print()
linguagens = {"Python", "Java", "PHP", "C"}


#inserindo um elemnto no set.
print(F'Antes {linguagens}')
linguagens.add("C#")
print(F'Depois {linguagens}')

print()
print()
#metodo update()
linguagens2 = {"Python", "Java", "PHP", "C"}

#inserindo mais de um elemento no set.
print(f'Antes {linguagens2}')
linguagens2.update(["Smalltalk", "Javascrip"])
print(f'Depois {linguagens2}')
print()