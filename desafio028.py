import random
from time import sleep
print('Olá, meu nome é Mr Magu, o programa que vai pensar em um número de 0 á 5 e você vai ter que adivinhar.\nSe caso você acertar o número que eu estou pensando, você ganha R$150,00!\nVamos começar?')
print('Vou pensar em um número...')
sleep(2)
print('Pronto!')
nunc = int(input('Me fale o número que você acha que é: '))
nun = random.randint(0, 5)
if nunc == nun:
    print('Parabéns você acaba de ganahr R$150,00!\nPorfavor passe na casa loterica mais próxima e retire seu dinheiro')
else:
    print('Não foi desta vez, pois o número que eu escolhi foi {}.'.format(nun))