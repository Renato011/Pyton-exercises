import random
print('Olá caso professor, eu sou o Robson, seu programa que ajuda a escolher um aluno aleatório na sala.\nPara isso eu preciso que você me diga o nome de quatro alunos.')
a1 = str(input('1° aluno: '))
a2 = str(input('2° aluno: '))
a3 = str(input('3° aluno: '))
a4 = str(input('4° aluno: '))
print('Muito bem, vou sortear um aluno entre {}, {}, {}, {}'.format(a1, a2, a3, a4))
print('O aluno escolhido aleatóriamente é: {}.'. format(random.choice([a1, a2, a3, a4])))