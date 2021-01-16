import math
co = float(input('Me diga o número de do cateto oposto e do cateto adjacente e vou lhe dizer qual a sua hipotenusa\nMe diga o primeiro cateto oposto: '))
ca = float(input('Agora me diga o outro cateto adjacente: '))
hy = math.hypot(co, ca)
print('A hipotenusa dos catetos a cima é {:.2f}.'.format(hy))

