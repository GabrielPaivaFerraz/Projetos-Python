class Pessoa:
    def __init__(self, nome, idade, nascimento):
        self.nome = nome
        self.idade = idade
        self.nascimento = nascimento

    def __str__(self):
        return f'''
        Nome: {self.nome}
        Data Nascimento: {self.nascimento}
        Idade: {self.idade}'''     
        