print("Olá caro pintor, meu nome é Genival um programa que vai te ajudar a calcular quantos metros de tinta você vai precisar usar para poder pinta a área desejada.")
larg = float(input('Muito bem, qual a largura do espaço em questão: '))
comp = float(input('Agora preciso saber qual o comprimento: '))
cont = larg*comp
tinta = cont/2
print('Vamos lá, para poder pintar a área desejada, você vai precisar usar {:.3f} litros de tinta.'.format(tinta))