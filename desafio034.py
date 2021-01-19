salario = float(input('Digite seu salário: '))
if salario <= 1250:
    sal1 = salario * 1.15
    print('seu novo salário é de {:.2f}'.format(sal1))
if salario > 1250:
    sal2 = salario * 1.10
    print('seu novo salário é de {:.2f}'.format(sal2))