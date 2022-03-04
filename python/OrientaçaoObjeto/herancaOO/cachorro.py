from calendar import c
import animal 

class Cachorro(animal.Animal):

    def __init__(self, nome, idade, peso):
        super().__init__(nome, idade, peso)