nun = int(input('Escolha um número inteiro: '))
print('Escolha uma das bases de conversão:\n[ 1 ] converter para BINÁRIO.\n[ 2 ] converter para OCTAL.\n'
      '[ 3 ] converter para HEXADECIMAL.')
opc = int(input('Digite sua opção: '))
if opc == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(nun, bin(nun)))
elif opc == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(nun, oct(nun)))
elif 3 == opc:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(nun, hex(nun) [2:]))
else:
    print('O valor digitado é inválido!')