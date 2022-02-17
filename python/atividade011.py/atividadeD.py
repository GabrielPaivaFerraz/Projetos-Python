# tecnico em informatica
#autor: Gabriel 
#data de inicio:10/02/2022
#data de termino:10/02/2022

import os

os.system('cls')

def conversao(temperatura):
    conversao = ((temperatura - 32) * 5) /9
    return conversao


print('-'*70)
print('Programa para converter temperatura')
print('='*70)

temperatura = float(input('informe a temperatura em Fahrenheit: '))

resultado = conversao(temperatura)

print('-'*70)
print(f'temperatura em fahrenheit: {temperatura}')
print(f'{temperatura} °F = {resultado:.1f} °C')
print('='*70)
print()