a = float(input('Me diga o valor da primeira reta: '))
b = float(input('Me diga o valor da segunda reta: '))
c = float(input('Me diga o valor da terceira e última reta: '))
if (b - c) < a < b + c and (a - c) < b < a + c and (a - c) < c < a + b:
    print('\033[33mSim, com esses valores você pode fazer um triângulo', end='') # , end='' é usado para colar uma linha na outra
    if a == b == c:
        print(' EQUILÁTERO!')
    elif a != b != c != a:
        print(' ESCALENO!')
    else:
        print(' ISÓSCELES!')
else:
    print('Não, com essas medidas não vai ser possível fazer um triângulo')