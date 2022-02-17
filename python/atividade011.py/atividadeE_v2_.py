# tecnico em informatica
#autor: Gabriel 
#data de inicio:14/02/2022
#data de termino:14/02/2022

import os
from math import pow

os.system('cls')


def calculo_imc(peso=0.0, altura=0.0):
    imc = peso / pow(altura, 2)

    if imc > 0 and imc <=20:
        return imc, 'Magro'
    elif imc > 20 and imc <= 24.9:
        return imc, 'Peso ideal'
    elif imc > 24.9 and imc <= 27:
        return imc, 'Sobrepeso'
    elif imc > 27 and imc <= 29.9:
        return imc, 'Obesidade leve'
    elif imc > 29.9 and imc <= 39.9:
        return imc, 'Obesidade'
    elif imc > 39.9 and imc <= 40:
        return imc, 'Obesidade morbida' 

print('-'*70)
print('Calcular o imc')
print('='*70)


try:
    peso = float(input('Informe seu peso: '))
    altura = float(input('Informe sua altura: '))

    resultado, situaçao = calculo_imc(peso, altura)

    print('-'*70)
    print(f'O calculo do imc e igual a {resultado:.2f}')
    print(f'Situaçao: {situaçao}')
    print('='*70)

except (ValueError, ZeroDivisionError, TypeError, NameError):
    print('Valor invalido') 
    print('-'*70)   