# tecnico em informatica
#autor: Gabriel 
#data de inicio:08/02/2022
#data de termino:11/02/2022

import os
os.system('cls')


def media_altura_peso(clientes):
    soma_altura = 0
    soma_peso = 0

    for registro in clientes:
        for chave, valor in registro.items():
            if chave == 'altura':
                soma_altura += valor 
            if chave == 'peso':
                soma_peso += valor 
        print()


    media_altura = soma_altura/len(clientes)
    media_peso = soma_peso/len(clientes)

    os.system('cls')
    print('PROGRAMA: ACADEMIA') 

    print('-'*70)
    print('Codigo \t\tNome \t\tAltura \t\tPeso') 
    print('='*70)

    for registro in clientes:
        for chave, valor in registro.items():
            print(f'{valor}', end='\t\t')
        print()

    print('-'*70)
    print('Media:', end='\t\t\t\t')
    print(f'{media_altura:.2f}', end='\t\t')
    print(f'{media_peso:.2f}', end='\t\t')
    print('='*70)


print('PROGRAMA: ACADEMIA')
print('='*70)

cliente = {}
clientes = []

while True:
    cliente['cod'] = int(input('Informe codigo do cliente: '))
    if cliente['cod'] == 0:
        break
    cliente['nome'] = str(input('Nome do cliente: '))
    cliente['altura'] = float(input('Informe sua altura: '))
    cliente['peso'] = float(input('informe seu peso: '))
    clientes.append(cliente.copy())

media_altura_peso(clientes)

