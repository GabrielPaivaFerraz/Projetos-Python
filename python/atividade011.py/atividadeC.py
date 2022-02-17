# tecnico em informatica
#autor: Gabriel 
#data de inicio:10/02/2022
#data de termino:10/02/2022

import os

os.system('cls')


def titulo():
    print('-'*70)
    print('aluno(a)\t\tMatricula\tNascimento')
    print('='*70)

def busca_aluno(cadastro_aluno):
    aluno = str(input('Entre com o nome do aluno: '))

    for item in cadastro_aluno:
        if item['nome'] == aluno:
            print('Encontrado!')
            return item
        else:
            break


cadastro_aluno = [
    {'nome' : 'Diana prince', 'matricula': '123456789', 'nascimento': 1960},
    {'nome' : 'Carol Danvers' , 'matriculas': '987654321', 'nascimento': 1970},
    {'nome' : 'Natalia Alianovna', 'matricula' : '951753258', 'nascimento': 1980},
]

titulo()
for item in cadastro_aluno:
    for c, v in item.items():
        print(f'{v}', end='     \t')
    print()
print('-'*70)
print()

resultado = busca_aluno(cadastro_aluno)

if resultado:
    titulo()
    for chave, valor in resultado.items():
        print(f'{valor}', end='     \t' )
    print()
    print('-'*70)

else:
    print('Aluno nao encontrado!')
    print('-'*70)
    print()
    

    