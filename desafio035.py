a = float(input('\033[1;37;44mMe diga o valor da primeira reta: '))
b = float(input('Me diga o valor da segunda reta: '))
c = float(input('Me diga o valor da terceira e última reta: '))
if (b - c) < a < b + c and (a - c) < b < a + c and (a - c) < c < a + b:
    print('\033[33mSim, com esses valores você pode fazer um triângulo')
else:
    print('Não, com essas medidas não vai ser possível fazer um triângulo')