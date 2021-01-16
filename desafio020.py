import random
print('Olá caso professor, eu sou o Joseval, seu programa que ajuda a escolher a ordem de apresentação dos trabalhos na sala.\nPara isso eu preciso que você me diga o nome de quatro alunos.')
a1 = str(input('1° aluno: '))
a2 = str(input('2° aluno: '))
a3 = str(input('3° aluno: '))
a4 = str(input('4° aluno: '))
print('Muito bem, vou sortear a ordem de apresentação dos trabalhos entre os alunos {}, {}, {}, {}'.format(a1, a2, a3, a4))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem escolhida aleatóriamente é:\n{}'.format(lista))