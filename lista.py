nomes = ['gustavo', 'jhon', 'pc',]
nomes1 = ['leticia','ingrid','brenda']
from random import randint
from time import sleep
escolhas = list()
escolhas1 = list()
certo = ' '
while True:
    for c in range (1,4):
        if c == 1:
            esc = randint(0,2)
            escolhas.append(esc)
            esc1 = randint(0,2)
            escolhas1.append(esc1)
            frase = (f'O {nomes[esc].title()} combina com {nomes1[esc1].title()}')
            print(frase)
            sleep(1)
        elif c == 2:
            while esc in escolhas:
                esc = randint(0,2)
            escolhas.append(esc)
            while esc1 in escolhas1:
                esc1 = randint(0,2)
            escolhas1.append(esc1)
            frase = (f'O {nomes[esc].title()} combina com {nomes1[esc1].title()}')
            print (frase)
            sleep(1)
        elif c == 3:
            while esc in escolhas:
                esc = randint(0,2)
            escolhas.append(esc)
            while esc1 in escolhas1:
                esc1 = randint(0,2)
            escolhas1.append(esc1)
            frase = (f'O {nomes[esc].title()} combina com {nomes1[esc1].title()}')
            print (frase)
            sleep(1)
            certo = ' '
            while certo not in 'SsNn':
                certo = input('Você acha certo? (S/N) ')
    if certo[0] in 'Ss':
        print ('Então ta bom')
        break
    else:
        escolhas.clear()
        escolhas1.clear()
