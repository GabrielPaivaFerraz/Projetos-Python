
class Retangulo:
    base = 0 
    altura = 0

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(base, altura):
        a = base * altura
        return a 

    def perimetro(base, altura):
        p = 2 * (base + altura)
        return p                