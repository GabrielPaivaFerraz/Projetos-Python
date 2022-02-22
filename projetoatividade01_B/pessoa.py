class Pessoa:
    def __init__(self, idade, nascimento):
        self.idade = idade
        self.nascimento = nascimento

    def __str__(self):
        return f'''
        Data Nascimento: {self.nascimento}
        Idade: {self.idade}'''     