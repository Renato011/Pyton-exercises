pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da sua PA: '))
decimo = pt + (11 - 1) * r
for n in range(pt,decimo, r):
    print(n)