print('Me diga as duas notas e vou lhe dizer se você passou de ano ou não.')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('\033[31mSua média foi {:.2f} você foi reprovado!'.format(media))
elif 7 > media >= 5: #jeiton parecido com a matemática
    print('\033[33mComo você tirou {:.2f}, você vai precisar ficar de recuperação.'.format(media))
elif media >= 7:
    print('\033[36mParabéns! Você foi aprovado!!!')