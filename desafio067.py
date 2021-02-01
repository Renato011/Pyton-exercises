while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 20)
    if num < 0:
        break
    for m in range (0, 11):
        print(f'{num} x {m} = {num * m}')
    print('-' * 20)
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')