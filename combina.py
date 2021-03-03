from time import sleep
from random import randint
eles = list()
elas = list()
cont = ' '
outro = ' '
while True:
    cont = ' '
    nome_dele = input('Escolha o JOGADOR: ').strip()
    while nome_dele in eles:
            sleep(1)
            print (f'{nome_dele} ja foi adicionado')
            sleep(1)
            nome_dele = input('Escolha o JOGADOR: ').strip()
    else:
        eles.append(nome_dele)
    nome_dela = input('Escolha a JOGADORA: ').strip()
    while nome_dela in elas:
        sleep(1)
        print(f'{nome_dela} ja foi adicionado')
        sleep(1)
        nome_dela = input('Escolha o JOGADOR: ').strip()
    else:
        elas.append(nome_dela)
    while cont[0] not in 'SsNn':
        cont = input('Deseja continuar: ').strip()
    if cont[0] in 'Nn':
        break
escolhas_eles = list()
escolhas_elas = list()
continuar = ' '
if len(eles) >= len(elas):
    while True:
        for c in range (1,len(eles)+1):
            if c == 1:
                esc = randint(0,len(eles)-1)
                escolhas_eles.append(esc)
                esc1 = randint(0,len(elas)-1)
                escolhas_elas.append(esc1)
                sleep(1)
                if eles[esc] == '':
                    eles[esc] = 'ninguem'
                if elas[esc1] == '':
                    elas[esc1] = 'ninguem'
                frase = (f'{eles[esc].title()} combina com {elas[esc1].title()}')
                print (frase)
                if 'ninguem' in eles:
                    eles.remove('ninguem')
                if 'ninguem' in elas:
                    elas.remove('ninguem')
            else:
                while esc in escolhas_eles:
                    esc = randint(0,len(eles)-1)
                escolhas_eles.append(esc)
                while esc1 in escolhas_elas:
                    esc1 = randint(0,len(elas)-1)
                escolhas_elas.append(esc1)
                if eles[esc] == '':
                    eles[esc] = 'ninguem'
                if elas[esc1] == '':
                    elas[esc1] = 'ninguem'
                frase = (f'{eles[esc].title()} combina com {elas[esc1].title()}')
                sleep(1)
                print (frase)
                if 'ninguem' in eles:
                    eles.remove('ninguem')
                if 'ninguem' in elas:
                    elas.remove('ninguem')


sleep(1)
print ('Finalizando...')
sleep(3)