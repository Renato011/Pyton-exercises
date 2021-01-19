from time import sleep
km = float(input('Quantos km você vai precisar percorrer: '))
print('CALCULANDO O PREÇO DA PASSAGEM...')
sleep(2)
if km <=200:
    print('o preço da passagem vai ser de R${:.2f}'.format(km*0.50))
else:
    print('O preço da passagrm vai ser de R${:.2f}'.format(km*0.45))