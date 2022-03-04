import os 
from curso import Curso

# Instanciando objetos
os.system('cls')

curso1 = Curso()

print(curso1.__nome) # nao encontra o atributo nome
print(curso1.versao)
print(curso1.ano)


print(f'{curso1.nome_curso()}: {curso1.ano_curso()}')

print()
