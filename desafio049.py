n = int(input('Me fale um número que lhe mostrarei a tabuada do mesmo: '))
print('-'*12)
for m in range(0, 11):
        print('{} x {:2} = {}'.format(n, m, n * m))
print('-'*12)