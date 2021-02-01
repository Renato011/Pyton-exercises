contidade = fsexo = mulher = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    if idade >= 18:
        contidade += 1
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if sexo == 'M':
            fsexo +=1
    if idade < 20 and sexo == 'F':
        mulher += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('-' * 20)
print(f'Total de pessoas com mais de 18 anos: {contidade}')
print(f'Ao todo temos {fsexo} homen cadastrado.')
print(f'E temos {mulher} com menos de 20 anos.')