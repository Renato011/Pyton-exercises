print('Bem vindo a Dublin shopping!')
pre = float(input('Qual o preço das compraa R$'))
print('''Formas de Pagamento:
[ 1 ] à vista no dinheiro ou cheque.
[ 2 ] à vista no cartão.
[ 3 ] 2x no cartão.
[ 4 ] 3x ou mais no cartão.''')
cond = int(input('Qual forma de pagamento você prefere acima, de 1 à 4: '))
if cond == 1:
    print("Com o pagamento à vista o valor vai sair R${:.2f}".format(pre * 0.9))
elif cond == 2:
    print('Com o pagamento à vista no cartão o preço vai ser R${:.2f}'.format(pre*0.95))
elif cond == 3:
    print('Parcelando em 2 vezes, consequimos manter o preço normal e ficara cada parcela de R${:.2f}'.format(pre/2))
elif cond == 4:
    con1 = int(input('Quantas parcelas você vai realizar a compra: '))
    pre1 = pre * 1.2
    par = pre1 / con1
    print("Dividindo em {} vezes, o valor do produto vai ser R${:.2f} e cada parcela vai ser R${:.2f}".format(con1, pre1, par))