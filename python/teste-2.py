#Curso técnico de informática
#Autor: Gabriel      
#Data de início: 06/11/2021
#termino: 06/11/2021

import os


os.system('cls')

#Título
print('-'*70)
print('SETS')
print('='*70)


#Declaração
idade = {1, 100}
nome = {'Clara', 'jane', 'Joe','Plabo' }
peso = {200}


print(f'nome : {nome} numero: {idade} peso: {peso}',end=' | ')
print()
print()

pergunta = str(input('deseja adicionar um nome?(s/n):')) 
if(pergunta == "s"):
    nome2 = str(input('Digite um nome:'))
    nome.add(nome2)


pergunta2 = str(input('Deseja adicionar sua idade?(s/n):'))    
if(pergunta2 == "s"):
    numero2= int(input('Digite sua idade:'))
    idade.add(numero2)


pergunta3 = str(input('Deseja adicionar seu peso?(s/n):'))   
if(pergunta3 == "s"):
    numero3 = float(input('Digite seu peso:'))
    peso.add(numero3)


print()
print('UNIÃO')
uniao = idade, peso .union(nome)
print(f'União de idade e peso com nome: {uniao}')
print()

