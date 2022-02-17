# tecnico em informatica
#autor: Gabriel 
#data de inicio:14/02/2022
#data de termino:14/02/2022


import os
from math import pow

os.system('cls')


def calculo_imc(peso=0.0, altura=0.0):
    imc = peso / pow(altura, 2)
    return imc

print('-'*70)
print('calcular o imc')
print('='*70)

try:
    peso = float(input('informe seu peso:'))
    altura = float(input('informe sua altura:'))
    
    resultado = calculo_imc(peso, altura)

    print('-'*70)
    print(f'o calculo do imc e igual a {resultado:.2f}')
    print('='*70)

except ValueError:
    print('valor invalido') 
    print('-'*70)
    print()   

