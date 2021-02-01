import random
cont = 0
print('=-=' * 10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-=' * 10)
while True:
    num = int(input('Diga um valor: '))
    classe = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()[0]
    numpc = random.randint(0, 11)
    soma = num + numpc
    resto = soma % 2
    print(f'Você jogou o número {num} e o computador {numpc}. Total de {soma} ', end='')
    if resto == 0:
        print(' e deu Par.')
        if classe == 'P':
            print('Você venceu!')
            print('Vamos jogar novamente...')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    if resto == 1:
        print('e deu Ímpar.')
        if classe == 'I':
            print('Você venceu!')
            print('Vamos jogar novamente...')
            cont +=1
        else:
            print('Você PERDEU!')
            break
print(f'GAME OVER! Você venceu {cont} vezes.')
