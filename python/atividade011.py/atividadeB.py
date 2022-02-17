# tecnico em informatica
#autor: Gabriel 
#data de inicio:10/02/2022
#data de termino:10/02/2022

import os

os.system('cls')

def cadastrar():
    alunos = {}
    lista = []
    for c in range(2):
        alunos['nome'] = str(input('nome do aluno: '))
        alunos['matricula'] = str(input('matricula do aluno: '))
        alunos['nascimento'] = str(input('data de nascimento do aluno: '))

        lista.append(alunos.copy())

        os.system('cls')
        print('-'*70)
        print('alunos cadastrados')
        print('='*70)

        for aluno in lista:
            for chave, valor in aluno.items():
                print(f'{chave} : {valor}', end=' ' + '\n')
            print('-'*80)  


print('-'*70)
print('cadastro de alunos')
print('='*70)
cadastrar()
