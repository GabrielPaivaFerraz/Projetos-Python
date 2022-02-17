#Curso técnico de informática
#Autor: Gabriel      
#Data de início: 06/11/2021
#termino: 06/11/2021


#Título
print('='*70)
print('')
print('='*70)

tuplaNome = ()

while (True):
    for c in range(0, 5):
        nome = str(input('Digite um nome: '))
        

        listaNome = list(tuplaNome)
        listaNome.append(nome)
        tuplaNome = tuple(listaNome)
#Saída
  

    print('nome: ', end=' | ')
    for nome in tuplaNome:
        print(nome, end=' | ')
    print()
    
        
    nomePosicao = str(input('Digite o nome que deseja saber a POSIÇÃO: '))
    indice = tuplaNome.index(nomePosicao)
    print(f'O nome {nomePosicao} aparece pela 1º vez na posição {indice}')
        
    
    print()
        
        
    nomeContar = str(input('Digite o nome que deseja saber sua ocorrência: '))      
    contar = tuplaNome.count(nomeContar)
    
    
    print(f'O nome {nomeContar} aparece {contar} vezes')
    print()
    print(f'FIM DO PROGRAMA!!!')
    print()
    print()


    


        


