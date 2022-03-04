class Curso:
    
    def __init__(self):
        self.__nome = 'Curso de python' # nome esta como privado (2 x __)
        self.versao = 3.10
        self.ano = 2020

    def nome_curso(self):
        return self.__nome # nome esta como privado (2 x __)

    def ano_curso(self):
        return self.ano        