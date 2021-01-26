s = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print('O somatório de todos os números impares de 0 até 500 é {} dentro dos valores {}!'.format(s, cont))