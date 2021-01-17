from time import sleep
print('Olá, meu nome é Robson, o seu radar inteligente.\nEstou aqui para ver se você foi multado e se sim, vou te dizere o valor da multa. ')
velo = float(input('Me diga a velocidade que o meliante passou: '))
print('ANALISANDO...')
sleep(2)
if velo >=80:
    print('Você recebeu uma multa meu rapaz.\nCom a velocidade de {:.2f} o valor a pagar vai ser de R${:.2f}.'.format(velo, (velo*7)))
if velo >=75<=79:
    print('Você não recebeu a multa, mas passou raspando!\nCuidado na próxima!')
if velo <=74:
    print('Parabén, você respeitou o limite de velocidade e pode seguir a viajem tranquilo!')
if velo <= 50:
        print('Mas você esta andando muito devagar para essa via. Tente ficar acima de 50km/h')
