from datetime import date
ano = int(input('Qual o ano que você nasceu: '))
ano1 = date.today().year
dif = ano1 - ano
print('O atleta que tem {} anos vai estar na categoria:'.format(dif))
if dif <= 9:
    print('Categoria mirim.')
elif dif <= 14:
    print('Categoria infantil.')
elif dif <= 19:
    print("Categoria junior.")
elif dif == 20:
    print('Categoria sênior.')
elif dif > 20:
    print('Categoria Master.')
