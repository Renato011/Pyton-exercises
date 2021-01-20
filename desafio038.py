print('Me fale dois números e te direi qual é o maior e o menor valor.')
pri = float(input('Primeiro valor: '))
seg = float(input('Segundo valor: '))
if pri > seg:
    print('O primeiro valor {:.0f} é maior.'.format(pri))
elif seg > pri:
    print('O segundo valor {:.0f} é maior.'.format(seg))
elif pri == seg:
    print('Os dois valores são iguais.')