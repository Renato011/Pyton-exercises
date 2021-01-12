print('Quer ver uma coisa curiosa?\nMe fale quantos reais você tem na sua carteira e eu direi quantos dollares você vai poder comprar.')
cash = float(input('Quantos reais você tem na sua carteira: R$'))
c = cash/3.27
print('Muito bem, com o dollar a R$3,27, você vai pode comprar ${:.2f}'.format(c))
