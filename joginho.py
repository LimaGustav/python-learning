#Introdução
from random import randint
from time import sleep
print ('=-'*15)
print ('{:^30}'.format('Joguinho do GUGA'))
print ('=-'*15)
sleep(3)
#Random
print ('Pensei em um número de 0 a 100')
sleep(2)
p = int(input('Melhor escolha de 0 até que número você quer que eu pense: '.strip()))
print(f'Pensei em um número de 0 a {p}')
print ('Tente adivinhar')
pc = randint(0,p)
sleep(3)
sleep(1)
chances = int(input('Quantas chances você quer? '))
c = 0
print (f'Você tera {chances} chances.')
sleep(1)
while c < chances:
    print (f'Você usou {c} chances, ainda restam {chances - c} chances ')
    sleep(1)
    c += 1
    jogador = int(input('Tente acertar: '))
    if pc < jogador:
        sleep(1)
        print ('Você errou, Pensei em um número Menor.')
    elif pc > jogador:
        sleep(1)
        print ('Você errou, Pensei em um número Maior')
    else:
        sleep(1)
        print (f'Você acertou pensei no número {pc}')
        break
if c == 5:
    print (f'Acabaram suas chances, eu pensei no número {pc}')