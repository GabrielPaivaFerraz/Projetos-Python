import os
import gato, cachorro, papagaio



os.system('cls')


gato = gato.Gato('Abel', 2, 5)
cachorro = cachorro.Cachorro('Thor', 5, 20)
papagaio = papagaio.Papagaio('Joaquin', 1, 1.5)


gato.miar()
cachorro.latir()
papagaio.falar()

