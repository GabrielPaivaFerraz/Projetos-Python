from conta import Conta
from carro import Carro
from pessoa import Pessoa

import os 
os.system('cls')

print('PROGRAMA PRINCIPAL-------------------------------------')
print()

print('Objetos do tipo pessoa---------------------------------')


gerente = Pessoa('John Doe', 50)
officeboy = Pessoa('Smith', 20)

print(f'\tNome: {gerente.nome}')
print(f'\tIdade: {gerente.idade}')


print('Obejetos do tipo carro---------------------------------')


gol = Carro('wolkwagen', 'Branca', 'BRA3049', 1985)
ferrari = Carro('F250', 'Vermelha', 'BRA6050', 2020)
prios = Carro('Toyota', 'Marrom','BRA9090', 2022)
print(f'\tFabricante: {gol.fabricante}')
print(f'\tCor: {gol.cor}')
print(f'\tPlaca: {gol.placa}')
print(f'\tAno: {gol.ano}')

print('Objeto do tipo conta-----------------------------------')


John = Conta('John Doe', 123456, 1550, 13)
Jane = Conta('Jane Doe', 654321, 2525, 15)

print(f'\tNome do Cliente: {John.cliente}')
print(f'\tAgencia: {John.agencia}')
print(f'\tNumero da Conta: {John.conta}')
print(f'\tDigito: {John.digito}')

print('-'*70)
