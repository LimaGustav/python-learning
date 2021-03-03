print ('=-'*15)
print ('{:^30}'.format('LOTOFACIL'))
print ('=-'*15)
from time import sleep
#Esquece
sleep(1)
from random import randint
continuar = ' '
while True:
    print ('Qual sua escolha? ')
    escolha = int(input('ALEATÓRIO [ 1 ]\nPADRÃO [ 2 ]\nOpção: '))
    if escolha == 1:
        loto = randint(1,25)
        numeros = list()
        jogos = int(input('Quantos jogos você deseja? '))
        for p in range (0,jogos):
            for c in range (0,15):
                if c == 0:
                    numeros.append(loto)
                else:
                    while loto in numeros:
                        loto = randint(1,25)
                    numeros.append(loto)
            numeros.sort()
            print (numeros)
            numeros.clear()
        continuar = input('Deseja continuar? (S/N) ')
        if continuar in 'Nn':
            print ('Finalizando...')
            sleep(2)
            break
    if escolha == 2:
        print (' ')
    else:
        sleep(1)