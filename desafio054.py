from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for press in range (1, 3):
    nasc = int(input('Qual a ano de nascimento da {}° pessoa: '.format(press)))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    elif idade < 18:
        totmenor += 1
print('Ao todo tivems {} pessoas maiores de idade.'.format(totmaior))
print('E também tivemos {} pessoas menores de idade!'.format(totmenor))
