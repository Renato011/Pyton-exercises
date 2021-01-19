'''print('Me diga três números e eu vou dizer qual é o maior e o menor.')
pri = float(input('Me diga o primeiro número: '))
seg = float(input('Me diga o segundo número: '))
ter = float(input('Me diga o terceiro número: '))
if pri > seg and pri > ter:
    print('O maior número é {:.0f}.'.format(pri))
if seg > pri and seg > ter:
    print('O maior número é {:.0f}.'.format(seg))
if ter > pri and ter > seg:
    print('O maior número é {:.0f}.'.format(ter))'''
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor'))
#Verificando o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor  = c
#Verificando o maior
maior  = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))