import os

from retangulo import Retangulo

os.system('cls')

retangulo1 = Retangulo
retangulo2 = Retangulo
retangulo3 = Retangulo
retangulo4 = Retangulo

print('CALCULOS PARA AREA E PERIMETRO DE UM RETANGULO')
print('-'*70)
resultado1 = retangulo1.area(10, 5)
resultado2 = retangulo2.area(100, 5)

print('AREA')
print(f'A area do retangulo e: {resultado1}')
print(f'A area do retangulo e: {resultado2}')
print('-'*70)

resultado3 = retangulo3.perimetro(10, 5)
resultado4 = retangulo4.perimetro(100, 5)

print('PERIMETRO')
print(f'O perimetro e: {resultado3}')
print(f'O perimetro e: {resultado4}')
print('-'*70)

print()