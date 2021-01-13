print('Olá, bem vindo a Dublin shopping, estamos no momento com um super saldão de descontos, me fale o preço do seu produto que lhe direi quanto custará com os 5% de desconto.')
pr = float(input('Me diga o preço do produto: R$'))
c = pr*0.95
print('O valor do produto com os 5% de desconto vai ser R${:.2f}'.format(c))