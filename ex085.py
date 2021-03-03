valores = [[],[]] #Valor[0] = par
for v in range (1,8):
    valor = int(input(f'Digite o {v}º valor: '))
    if valor % 2 == 0:
        while valor in valores[0]:
            print ('Valor ja adicioanado')
            valor = int(input(f'Digite o {v}º valor: '))
        else:
            valores[0].append(valor)
    else:
        while valor in valores[1]:
            print ('Valor ja adicionado')
            valor = int(input(f'Digite o {v}º valor: '))
        else:
            valores[1].append(valor)
valores[0].sort()
valores[1].sort()
print (f'Os valores pares digitados foram {valores[0]}')
print (f'Os valores impares digitados foram {valores[1]}')