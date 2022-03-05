import os
from girafa import Girafa
from sardinha import Sardinha
from papagaio import Papagaio


os.system('cls')

peixe = Sardinha()
girafa = Girafa()
passaro = Papagaio()

print('-'*70)
peixe.locomover()
girafa.locomover()
passaro.locomover()
print('-'*70)

