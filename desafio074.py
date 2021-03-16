import random
sort = random.randint(0, 5), random.randint(0, 9),\
       random.randint(0, 5), random.randint(0, 5), random.randint(0, 5)
print(f'Os valores sorteados foram: ', end='')
for n in sort:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi: {max(sort)}')
print(f'O menor valor sorteado foi: {min(sort)}')