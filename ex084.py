pessoas = list()
dados = list()
mai = men = 0
while True:
    cont = ' '
    dados.append(input('Nome: ').strip().title())
    dados.append(float(input('Peso: ').strip()))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] < men:
            men = dados[1]
        if dados[1] > mai:
            mai = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    while cont[0] not in 'NnSs':
        cont = input('Deseja continuar? (S/N) ').strip()
    if cont[0] in 'Nn':
        break
print (f'Você cadastrou {len(pessoas)} pessoas')
print (f'O mair peso foi {mai}, Peso de',end='. ')
for p in pessoas:
    if p[1] == mai:
        print (f'[{p[0]}]',end=' ')
print (f'\nO menor peso foi {men}, Peso de',end='. ')
for p in pessoas:
    if p[1] == men:
        print (f'[{p[0]}]',end=' ')