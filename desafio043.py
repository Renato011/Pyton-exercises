print('Olá meu nome é Aroudo seu programa médico que lhe calculará seu IMC.')
peso = float(input('Me diga o seu peso: '))
alt = float(input('Me diga a sua altura: '))
imc = peso / (alt**2)
print('Com o IMC {:.1f} você vai estar com '.format(imc), end='')
if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= imc < 25: # modo que o python aceita.
    print('Peso ideal.')
elif imc > 25 and imc <= 30: # modo tradicional.
    print('Sobrepeso.')
elif imc > 30 and imc <= 40:
    print('Obesidade.')
elif imc > 40:
    print('Obesidade mórbida.')
