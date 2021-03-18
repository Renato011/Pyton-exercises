listanum = []
while True:
    num = int(input('Digite um valor: '))
    if num in listanum:
        print('Valor Duplicado! Não vou adicionar...')
    else:
        listanum.append(num)
        print('Valor adicionado com sucesso...')
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if opcao == 'N':
        break
listanum.sort()
print(listanum)
