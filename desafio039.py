from datetime import date
ano = int(input('Me diga o ano que voçê nasceu e direi se está na hora de se alistar ou não.\nQual o ano que você nasceu: '))
ano1 = date.today().year # para saber o ano quando que o computador está.
dif = ano1 - ano # subtração para saber se tem mais ou menos que 18 anos.
dif1 = 18 - dif
if dif <= 17:
    print('Ainda não é hora de se alistar, espere mais {} anos para poder se alista.'.format(dif1))
elif dif == 18:
    print('Este é o ano que você completa 18 anos, você tem que se alistar!')
elif dif >= 19:
    print('Você está com {:.0f} anos, já passou da hora de alistar, corra para a junta militar da sua cidade!'.format(dif))