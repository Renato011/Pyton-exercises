s = 0 # base de soma
for r in range (0, 4): # número de perguntas que eu quero fazer
    n = int(input('Digite um número: ')) # valor adicionado ao programa
    if n % 2 == 0: # verificar se os números digitados são pares
        s += n # usar a base com a soma dos números pares. a base serve para indicar que os números destro do for é para ser somado
print('A soma dos números pares da sua lista vai ser {}.'.format(s))


