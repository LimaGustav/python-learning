matrix = [[0,0,0],[0,0,0],[0,0,0]]
pares = 0
for c in range (0,3):
    for l in range(0,3):
        matrix[c][l] = input(f'Digito o valor ({c+1},{l+1}) ')
print ('=-'*20)
for c in range (0,3):
    for v in range (0,3):
        print (f'[{matrix[c][v]:^5}]',end=' ')
    print()
print (f'A soma dos valores pares é de {pares}')
