# tecnico em informatica
#autor: Gabriel 
#data de inicio:21/02/2022
#data de termino:22/02/2022

import os
from bissexto import Bissexto

os.system('cls')


print('-'*50)
print('PROGRAMA PARA CALCULAR ANO BISSEXTO')
print('='*50)


#Entrada de Dados:
a = int(input('Insira o ano desejado: '))


#Instanciando:
ano = Bissexto

#Invocando a classe:
ano.conta(a)
print()