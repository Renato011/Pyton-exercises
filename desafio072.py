num = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',\
      'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte'
while True:
    numc = (int(input('Digite um número de 0 a 20: ')))
    if 0 <= numc <=20:
        break
print(f'Você digitou o número {num[numc]}.')
