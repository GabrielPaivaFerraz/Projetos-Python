import os 
from curso import Curso

# Instanciando objetos
os.system('cls')

curso1 = Curso()

curso1.set__nome('Curso Python')
print(curso1.versao)
print(curso1.ano)


print(f'{curso1.nome_curso()}: {curso1.ano_curso()}')

print()
