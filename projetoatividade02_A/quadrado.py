class Quadrado:
    largura = 0 
    altura = 0

    def __init__(self, largura, altura):
        self.base = largura
        self.altura = altura

    def largura1(largura, altura):
        l = largura* altura
        return l

    def altura1(largura, altura):
        a = 2 * (largura + altura)
        return a               