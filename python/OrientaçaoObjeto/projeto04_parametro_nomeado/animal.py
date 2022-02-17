class Animal:
    
    def __init__(self, nome='sem nome', raca='labrador', nascimento=1970):
        
        self.nome = nome
        self.raca = raca
        self.nascimento = nascimento

    def __str__(self):
        return f''' 
        Nome: {self.nome} 
        Data Nascimento: {self.nascimento}
        Raca:{self.raca} '''  
