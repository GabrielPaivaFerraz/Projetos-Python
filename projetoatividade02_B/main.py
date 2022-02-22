# tecnico em informatica
#autor: Gabriel 
#data de inicio:21/02/2022
#data de termino:22/02/2022

import os
from triangulo import Triangulo

os.system('cls')


print('-'*50)
print('PROGRAMA PARA CALCULAR EXIST~ENCIA DE UM TRIÂNGULO')
print('-'*50)

#Entrada de Dados
a = int(input('Informe o segmento "a": '))
b = int(input('Informe o segmento "b": '))
c = int(input('Informe o segmento "c": '))

triangulo = Triangulo

triangulo.conta(a, b, c)
