matrix = [[0,0,0],[0,0,0],[0,0,0]]
# Constroi matrix
for c in range (0,3):
    for l in range (0,3):
        matrix[c][l] = int(input(f'Digite o número da posição ({c+1},{l+1}) '))
# Printa a matrix
print ('=-'*15)
for c in range (0,3):
    for l in range (0,3):
        print(f'[{matrix[c][l]:^6}]',end=' ')
    print()
print