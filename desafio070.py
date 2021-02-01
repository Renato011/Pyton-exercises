print('-' * 20)
print('LOJA SUPER BARATÃO')
print('-' * 20)
total = caro = menor = cont = 0
barato = ' '
while True:
    prod = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        caro += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = prod
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' Fim do programa '))
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {caro} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {prod} que custa R${menor}')