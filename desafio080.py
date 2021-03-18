listanum = []
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > listanum[-1]:
        listanum.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(listanum):
            if num <= listanum[pos]:
                listanum.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram: {listanum}')