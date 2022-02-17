#importando as bibliotecas

import os 

os.system('cls')

print('='*80) 
print('Dicionarios: metodo copy ()')
print('='*80)

#Declaraçao 
agenda = {
    'jojo' : '99196-3030',
    'Dio' : '99196-5050',
    'Jolyne' : '99196-6060',
    'Lisa Lisa' : '99196-7070',
    'Speedwagon' : '99196-8080',

}

#saida com for 
print('Nome \t\t\tCelular')
print('-'*80)
for chave, valor in agenda.items():
    print(f'{chave}     \t\t{valor}')
print('-'*80)
print()    
