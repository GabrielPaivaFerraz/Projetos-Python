class Bissexto:
    
    
    def __init__(self, a):
        
        self.a = a 

    def conta(a):

        if (a <= 0):
             print('Ano invalido!')
        elif (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
            print(f'O ano {a} e bissexto! ') 

        else:
            print(f'O ano {a} nao e bissexto')          