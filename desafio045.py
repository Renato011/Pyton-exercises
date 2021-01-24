import emoji
import random
print('E ai, bora jogar um Jakenpô?!\nEscolha uma das opções abaixo:')
jogador = int(input(emoji.emojize('1 = Pedra :raised_fist:\n2 = Papel :raised_hand:\n3 = Tesoura :victory_hand:\nQual '
                                  'você escolhe: ')))
pedra = emoji.emojize(':raised_fist:')
papel = emoji.emojize(':raised_hand:')
tesoura = emoji.emojize(':victory_hand:')
pc = random.choice([pedra, papel, tesoura])
if jogador == 1 and pc == pedra:
    print('{} + {} Muito bem, empatamos.\nVamos jogar de novo.'.format(pedra,pedra))
elif jogador == 1 and pc == papel:
    print('{} + {} Ganhei de você!'.format(pedra, papel))
elif jogador == 1 and pc == tesoura:
    print('{} + {} Você ganhou essa, quero revanche!'.format(pedra,tesoura))
elif jogador == 2 and pc == papel:
        print('{} + {} Muito bem, empatamos.\nVamos jogar de novo.'.format(papel, papel))
elif jogador == 2 and pc == tesoura:
        print('{} + {} Ganhei de você!'.format(papel, tesoura))
elif jogador == 2 and pc == pedra:
        print('{} + {} Você ganhou essa, quero revanche!'.format(papel, pedra))
elif jogador == 3 and pc == tesoura:
    print('{} + {} Muito bem, empatamos.\nVamos jogar de novo.'.format(tesoura,tesoura))
elif jogador == 3 and pc == pedra:
    print('{} + {} Ganhei de você!'.format(tesoura, pedra))
elif jogador == 3 and pc == papel:
    print('{} + {} Você ganhou essa, quero revanche!'.format(tesoura,papel))