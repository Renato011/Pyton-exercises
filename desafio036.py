print('Olá, meu nome é Arlindo o sistema de empréstimo que vai te ajudar a conquistar sua casa.\nPara realizar o seu empréstimo vou precisar de 3 informações muito importante, sendo elas:')
valor = float(input('Qual o valor da casa em vista: R$'))
salario = float(input('Qual o salário atual: R$'))
ano = float(input('Em quantos anos você pretende pagar o empréstimo: '))
vpagar = (valor/(ano*12))
vcento = salario*0.30
'''print('{:.2f}'.format(vcento))'''
if vpagar < vcento:
    print('\33[36mMuito bem, seu empréstimo vai ser consedido com sucesso! ')
else:
    print('\33[31mMe desculpe, mas com o salário de R${:.2f} ao mês, não vamos conseguir fazer seu empréstimo!'.format(salario))