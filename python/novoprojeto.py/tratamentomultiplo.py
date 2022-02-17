# tecnico em informatica
#autor: Gabriel 
#data de inicio:07/02/2022
#data de termino:07/02/2022


from distutils.log import error
import os 

os.system('cls')

def erro(a):
    try:
        eval(a)
    except TypeError:
        print('TypeError: impossivel realizar a operaçao!')
    except NameError:
        print('NameError: variavel nao foi definida!')
    except ValueError:
        print('ValuerError: tentando converter um literal em um inteiro!')


#saida
print('-'*70)
print(error('int + int'))
print(error('var')) 
print(error('int("a")'))
print('-'*70)
print()
                   