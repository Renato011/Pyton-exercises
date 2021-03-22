lista = []
pares = []
impares = []
while True:
    num = int(input('Digite um valor:'))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if opcao == 'N':
        break
print('-=' * 30)
print(f'Alista completa é {lista}')
print(f'A lista de números pares é: {pares}')
print(f'A lista de números ímpares é: {impares}')
