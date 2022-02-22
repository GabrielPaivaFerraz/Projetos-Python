# tecnico em informatica
#autor: Gabriel 
#data de inicio:21/02/2022
#data de termino:22/02/2022


import os

from quadrado import Quadrado

os.system('cls')

quadrado1 = Quadrado
quadrado2 = Quadrado
quadrado3 = Quadrado
quadrado4 = Quadrado


print('CALCULOS PARA LARGURA E ALTURA DE UM QUADRADO')
print('-'*70)

resultado1 = quadrado1.largura1(20, 5)
resultado2 = quadrado2.largura1(80, 5)

print('LARGURA')
print(f'A largura do quadrado e:{resultado1}')
print(f'A largura do quadrado e:{resultado2}')
print('-'*70)

resultado3 = quadrado3.altura1(20, 5)
resultado4 = quadrado4.altura1(80, 5)

print('ALTURA')
print(f'O altura do quadrado e: {resultado3}')
print(f'O altura do quadrado e: {resultado4}')
print('-'*70)
